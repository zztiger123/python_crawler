import requests
import re


# 设置 http 请求头伪装成浏览器
send_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"}

# regex_category = r"\"dest\":\"(.*)\",\"ab\":\"new\"}'>[\s]*?<(.*)>[\s]*?<span class=\"title oneline\">[\s]*?<span class=\"text\">(.*)<\/span>[\s]*?<\/span>[\s]*?<span class=\"count float-right\">([\d]+)篇<\/span>"
# regex_blog = r"<a href=\"(.*)\" target(.*)>[\s]+<div class=\"column_article_title\">[\s]+<(.*)>[\s]+<(.*)>[\s]+(.*)[\s]+"

regex_category = r"<li class=\"toctree-l1\"><a class=\"reference internal\" href=\"(.*?)\">(.*?)</a></li>"
regex_topic = r"<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"(.*?)\">(.*?)</a></li>"
regex_subtopic = r"<li class=\"toctree-l1\"><a class=\"reference internal\" href=\"(.*?)\">(.*?)</a></li>"
regex_question = r"<li class=\"toctree-l3\"><a class=\"reference internal\" href=\"(.*?)\">(.*?)</a></li>"
regex_subtopic_question = r"<h2>(.*)<a class=\"headerlink\" href=\"(.*)\" title="

faq_url = f'https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/index.html'

# 使用正则表达式抓取需要的文本
def get_text_from_url_by_regex(url, regex):
	html = requests.get(url, headers=send_headers)
	if html.status_code != 200:
		print(html + ' status = ' + html.status_code)

	else:
		html.encoding = "utf-8"
		html_str = html.text
		
		text_result = re.findall(regex,html_str)

		return text_result

# 从 FAQ 主页获取每个大的分类
def get_category_link_from_faq_url(url):
	print(url)
	category_content = ''

	all_categorys = get_text_from_url_by_regex(url, regex_category)
	all_categorys_str = str(all_categorys)
	str_url = str(url)

	if all_categorys_str.strip()=='[]':
		print("not found ")
	else:
		category_count = 1
		for category in all_categorys[0:]:
			category_str = str(category)

			faq_category_url = str_url.replace("index.html", category[0])

			category_content = f'\n## {category_count} [{category[1]}]({faq_category_url}) \n'



			with open('public_faq_summary.md','a+',encoding='utf-8') as f:
				f.write('\n\n-------------------------------------------------------')
				f.write(category_content)
				print(category_content)

			get_topic_link_from_faq_category_url(faq_category_url, category_count)
			category_count += 1			

	category_count = 0

# 从 FAQ 每个大的分类获取对应的子版块
def get_topic_link_from_faq_category_url(url, count):
	print(url)
	category_content = ''

	all_categorys = get_text_from_url_by_regex(url, regex_topic)
	all_categorys_str = str(all_categorys)
	str_url = str(url)

	print(111)

	if all_categorys_str.strip()=='[]':
		print("not found ")
	else:
		topic_count = 1
		print(all_categorys)
		for category in all_categorys[0:]:
			category_str = str(category)

			faq_topic_url = str_url.replace("index.html", category[0])

			category_content = f'\n### {count}.{topic_count} [{category[1]}]({faq_topic_url}) \n'

			with open('public_faq_summary.md','a+',encoding='utf-8') as f:
				f.write(category_content)
				print(category_content)

			if faq_topic_url.count("index") > 0:
				get_subtopic_link_from_faq_topic_url(faq_topic_url, count, topic_count) #如果分类里有子分类，调用此 API
			else:
				get_question_link_from_faq_category_url(faq_topic_url, False)
			
			topic_count += 1

	topic_count = 0

# 从 FAQ 每个子版块获取更小的子版块（如有）
def get_subtopic_link_from_faq_topic_url(url, count, topic_count):
	print(url)
	category_content = ''

	all_categorys = get_text_from_url_by_regex(url, regex_subtopic)
	all_categorys_str = str(all_categorys)
	str_url = str(url)

	print(111)

	if all_categorys_str.strip()=='[]':
		print("not found ")
	else:
		subtopic_count = 1
		print(all_categorys)
		for category in all_categorys[0:]:
			category_str = str(category)
			if category[0].count("..") > 0:
				continue

			faq_topic_url = str_url.replace("index.html", category[0])

			print('faq url ------------' + faq_topic_url)


			category_content = f'\n#### {count}.{topic_count}.{subtopic_count}  [{category[1]}]({faq_topic_url}) \n'
			subtopic_count += 1


			with open('public_faq_summary.md','a+',encoding='utf-8') as f:
					f.write(category_content)
					print(category_content)
				
			get_question_link_from_faq_category_url(faq_topic_url, True)
		
	
		subtopic_count = 0


# 从 FAQ 每个子版块获取对应的 Q & A
def get_question_link_from_faq_category_url(url,is_subtopic):
	print(url)
	category_content = ''

	if is_subtopic == True:
		all_categorys = get_text_from_url_by_regex(url, regex_subtopic_question)
	else:
		all_categorys = get_text_from_url_by_regex(url, regex_question)
	all_categorys_str = str(all_categorys)

	if all_categorys_str.strip()=='[]':
		print("not found ")
	else:
		count = 1
		for category in all_categorys[1:]:
			category_str = str(category)

			if is_subtopic == True:
				faq_question_url = url + category[1]
				category_content = f'\n- {count} [{category[0]}]({faq_question_url}) \n'
			else:
				faq_question_url = url + category[0]
				category_content = f'\n- {count} [{category[1]}]({faq_question_url}) \n'

			count += 1

			with open('public_faq_summary.md','a+',encoding='utf-8') as f:
				f.write(category_content)
				print(category_content)

	count = 0
		

if __name__=="__main__":

	with open('public_faq_summary.md','a+',encoding='utf-8') as f:
		f.write("# 公开的 FAQ 汇总")

	# get_category_link_from_csdn_url(csdn_url)
	get_category_link_from_faq_url(faq_url)
