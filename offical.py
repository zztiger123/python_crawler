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

regex_category = r"<a href=\"(.*?)\" target=\"_blank\" data-report-click=\"{(.*?) <span title=\"(.*?)\"(.*?)</span> <!----></a> <(.*?)>(.*?)篇"
regex_blog = r"<a href=\"(.*)\" target(.*)[\s]+(.*)[\s]+<h2 class=\"title\">[\s]+(.*)"

csdn_url = f'https://blog.csdn.net/Marchtwentytwo'

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

# 从 csdn 小号主页获取专栏名称
def get_category_link_from_csdn_url(url):
	print(url)
	category_content = ''

	all_categorys = get_text_from_url_by_regex(url, regex_category)
	all_categorys_str = str(all_categorys)

	if all_categorys_str.strip()=='[]':
		print("not found ")
	else:
		count = 1
		for category in all_categorys:
			category_str = str(category)
			category_content =f'\n## {count} [{category[2]}]({category[0]}) ： 一共 {category[5]} 篇博客\n'

			count += 1

			with open('csdn_blog_summary.md','a+',encoding='utf-8') as f:
				f.write('\n\n-------------------------------------------------------')
				f.write(category_content)
				print(category_content)
			get_blog_link_from_category(category[0])

	count = 0

# 从 csdn 专栏里获取博客标题和对应的链接
def get_blog_link_from_category(url):
	index = 1

	html_str = '.html'
	url = url.rstrip(html_str)

	while True:
		blog_content = ''
		page_url = ''
		url_now = ''
		if index > 1:
			page_url = f'_{index}.html'
			url_now = url + page_url
		else:
			url_now = url + html_str

		print(url_now)

		all_blogs = get_text_from_url_by_regex(url_now, regex_blog)
		all_blogs_str = str(all_blogs)

		if all_blogs_str.strip()=='[]':
			print("not found ")
			break
		else:
			print("get blog name ")
			for blog in all_blogs:
				blog_str = str(blog)

				blog_content = f'{blog_content}\n - [{blog[4]}]({blog[0]})'
				pass

		with open('csdn_blog_summary.md','a+',encoding='utf-8') as f:
			f.write(blog_content)

		index += 1
		

if __name__=="__main__":

	with open('csdn_blog_summary.md','a+',encoding='utf-8') as f:
		f.write("# CSDN 小号博客汇总")

	get_category_link_from_csdn_url(csdn_url)
