# 公开的 FAQ 汇总

-------------------------------------------------------
## 1 [使用说明](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/instruction/index.html) 

### 1.1 [问题查找](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/instruction/question-search.html) 

### 1.2 [文档贡献](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/instruction/document-contribution.html) 

- 1 [分支命名规范](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/instruction/document-contribution.html#id6) 

- 2 [本地编译环境](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/instruction/document-contribution.html#id10) 

- 3 [提交信息规范](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/instruction/document-contribution.html#id11) 


-------------------------------------------------------
## 2 [开发环境](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/index.html) 

### 2.1 [IDE 插件](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/IDE-plugins.html) 

- 1 [使用 Arduino IDE 开发平台，如何读取 ESP32 出厂自带的 Wi-Fi 的 MAC 地址？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/IDE-plugins.html#arduino-ide-esp32-wi-fi-mac) 

- 2 [如何使用 flash download tool 将基于 Arduino 开发生成的 bin 文件烧录到 ESP32？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/IDE-plugins.html#flash-download-tool-arduino-bin-esp32) 

### 2.2 [调试分析](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html) 

- 1 [ESP32 如何关闭默认通过 UART0 发送的调试信息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp32-uart0) 

- 2 [ESP32 如何修改默认上电校准⽅式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp32) 

- 3 [ESP8266 如何修改默认上电校准⽅式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp8266) 

- 4 [ESP32 boot 启动模式不正常如何排查？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp32-boot) 

- 5 [使用 ESP32 JLINK 调试，发现会报 ERROR：No Symbols For Freertos，如何解决呢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp32-jlink-error-no-symbols-for-freertos) 

- 6 [如何监测任务栈的剩余空间？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#id3) 

- 7 [ESP32-S2 是否可以使用 JTAG 进行下载调试？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp32-s2-jtag) 

- 8 [如何在不更改 menuconfig 输出级别的情况下调整日志输出？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#menuconfig) 

- 9 [为什么 ESP8266 进⼊启动模式（2，7）并触发看⻔狗复位？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp8266-2-7) 

- 10 [ESP-WROVER-KIT 开发板 openocd 错误 Error: Can’t find board/esp32-wrover-kit-3.3v.cfg？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp-wrover-kit-openocd-error-can-t-find-board-esp32-wrover-kit-3-3v-cfg) 

- 11 [ESP32 SPI boot 时会一直发生 RTC_watch_dog 复位是什么原因?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp32-spi-boot-rtc-watch-dog) 

- 12 [ESP32 如何获取与解析 coredump？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp32-coredump) 

- 13 [ESP32&amp;ESP8266&amp;ESP32S2 如何做射频性能测试？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp32-esp8266-esp32s2) 

- 14 [Win 10 系统下识别不到设备有哪些原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#win-10) 

- 15 [ESP32 出现 Error:Core 1 paniced (Cache disabled but cache memory region accessed) 是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp32-error-core-1-paniced-cache-disabled-but-cache-memory-region-accessed) 

- 16 [如何读取模组 Flash 型号信息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#flash) 

- 17 [调试 ESP-IDF 里的 Ethernet demo，出现如下异常日志？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp-idf-ethernet-demo) 

- 18 [使用 ESP32 时出现 “Brownout detector was triggered” 报错原因是什么，以及如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp32-brownout-detector-was-triggered) 

- 19 [导入头文件 protocol_examples_common.h 后，为什么编译时提示找不到该文件?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#protocol-examples-common-h) 

- 20 [使用 ESP8266 NonOS v3.0 版本的 SDK，如下报错是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/debugging.html#esp8266-nonos-v3-0-sdk) 

### 2.3 [环境搭建](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/environment-setup.html) 

- 1 [idf.py menuconfig 编译报 “Configuring incomplete, errors occured” 的错误信息如何解决呢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/environment-setup.html#idf-py-menuconfig-configuring-incomplete-errors-occured) 

- 2 [Windows 下使用 ESP-IDF Tools 2.3 工具安装 master 版本的 esp-idf 出现错误：Installation has failed with exit code 2，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/environment-setup.html#windows-esp-idf-tools-2-3-master-esp-idf-installation-has-failed-with-exit-code-2) 

- 3 [Windows 下使用 esp-idf-tools-setup-2.3.exe 搭建环境，运行 <code class="docutils literal notranslate"><span class="pre">make</span> <span class="pre">menuconfig</span></code> 出现如下错误：](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/environment-setup.html#windows-esp-idf-tools-setup-2-3-exe-make-menuconfig) 

- 4 [Windows 下使用 esp-idf-tools-setup-2.2.exe 安装过程中，出现 python 工具异常：](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/environment-setup.html#windows-esp-idf-tools-setup-2-2-exe-python) 

- 5 [Windows 下安装编译环境出现 <code class="docutils literal notranslate"><span class="pre">Download</span> <span class="pre">failed:</span> <span class="pre">安全频道支持出错</span></code>？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/environment-setup.html#windows-download-failed) 

- 6 [Windows 下执行 export.bat，提示 CMake、gdbgui 版本错误：](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/environment-setup.html#windows-export-bat-cmakegdbgui) 

- 7 [将版本从 v3.3 更新至最新版本后，使用 idf.menuconfig 及 idf.build 报错：](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/environment-setup.html#v3-3-idf-menuconfig-idf-build) 

- 8 [如果同时要开发 ESP32 和 ESP8266，该怎样设置 <code class="docutils literal notranslate"><span class="pre">PATH</span></code> 和 <code class="docutils literal notranslate"><span class="pre">IDF_PATH</span></code>？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/environment-setup.html#esp32-esp8266-path-idf-path) 

- 9 [每一次切换项目时都需要重新调用 <code class="docutils literal notranslate"><span class="pre">idf.py</span> <span class="pre">set-target</span></code> 指令吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/environment-setup.html#idf-py-set-target) 

- 10 [如何查看当前 ESP-IDF 的版本号，是否存在记录版本号的文件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/environment-setup.html#esp-idf) 

- 11 [Windows 环境下 ESP-IDF 编译比较慢如何优化？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/environment-setup.html#windows-esp-idf) 

### 2.4 [固件升级](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html) 

- 1 [如何使用 USB 转串口工具对 ESP32 系列的模组下载固件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#usb-esp32) 

- 2 [macOS 与 Linux 如何烧录固件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#macos-linux) 

- 3 [ESP32 是否支持使用 JTAG 管脚直接烧写程序？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#esp32-jtag) 

- 4 [ESP_Flash_Downloader_Tool 是否可以自定义编程控制？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#esp-flash-downloader-tool) 

- 5 [ESP32 能否通过 OTA 开启 Security Boot 功能？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#esp32-ota-security-boot) 

- 6 [基于 ESP-IDF v4.1 编译固件烧录到 ESP32-S2 设备的过程中遇到如下错误，该如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#esp-idf-v4-1-esp32-s2) 

- 7 [如何使用 flash_download_tool 下载基于 esp-idf 编译的固件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#flash-download-tool-esp-idf) 

- 8 [ESP 芯片烧录通讯协议是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#esp) 

- 9 [如何对 ESP32-C3 进行离线程序烧录？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#esp32-c3) 

- 10 [ESP32 如何设置 Flash SPI 为 QIO 模式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#esp32-flash-spi-qio) 

- 11 [使用 ESP8266 开发板，下载程序后，上电启动串口打印如下日志，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#esp8266) 

- 12 [乐鑫模组烧录工具有那些？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#id8) 

- 13 [Flash 下载工具 的工厂模式和开发者模式有什么区别？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#id10) 

- 14 [ESP32-C3 芯片可以使用 USB 进行固件的下载，但在 ESP-IDF v4.3 下使用并不支持，如何使用 USB 进行固件下载？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#esp32-c3-usb-esp-idf-v4-3-usb) 

- 15 [一拖四治具工厂模式烧写失败原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#id11) 

- 16 [使用 ESP32-WROVER-B 模组通过 Flash 下载工具 下载 AT 固件，当完成写 Flash 后，结果显示 ERROR。但使用 ESP32-WEOVER-E 的模组下载相同的 AT 固件结果却显示正常，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#esp32-wrover-b-flash-at-flash-error-esp32-weover-e-at) 

- 17 [为什么使用 Flash 下载工具 无法重新烧录已加密设备？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#id14) 

- 18 [基于 esptool 串口协议 通过 UART 接口对 ESP32 进行刷新固件，是否可以新增一个 app 分区？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#esptool-uart-esp32-app) 

- 19 [使用 ESP8266 通过 Flash 下载工具 ，下载程序固件后无程序运行日志输出，串口打印如下，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#esp8266-flash) 

- 20 [Windows7 系统 USB 驱动无法识别是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#windows7-usb) 

- 21 [使用 ESP32-WROVER-E 模组下载程序后，上电打印日志如下，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/development-environment/firmware-update.html#esp32-wrover-e) 


-------------------------------------------------------
## 3 [应用方案](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/index.html) 

### 3.1 [AI 应用](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/artificial-intelligence.html) 

- 1 [esp-who 是否⽀持 IDF 4.1？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/artificial-intelligence.html#esp-who-idf-4-1) 

- 2 [esp-face组件的api参考？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/artificial-intelligence.html#esp-faceapi) 

- 3 [请问微信小程序esp-eye有相关资料吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/artificial-intelligence.html#esp-eye) 

- 4 [ESP 模块是否支持 TensorFlow？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/artificial-intelligence.html#esp-tensorflow) 

- 5 [esp-skainet 示例支持哪些语言呢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/artificial-intelligence.html#id2) 

### 3.2 [AT 命令](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html) 

- 1 [ESP8266 v2.1.0.0 版本 AT 固件，如何关闭默认的 power save 模式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#esp8266-v2-1-0-0-at-power-save) 

- 2 [发送 AT 命令，返回如下日志，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#id1) 

- 3 [AT+BLEGATTSNTFY 和 AT+BLEGATTSIND 的 length 最大可以支持到多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#at-blegattsntfy-at-blegattsind-length) 

- 4 [ESP8266 NONOS AT 固件如何使能全校准模式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#esp8266-nonos-at) 

- 5 [ESP32 AT BLE UART 透传的最大传输率是？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#esp32-at-ble-uart) 

- 6 [如何获取到模组 ESP32-MINI-1(内置芯片 ESP32-U4WDH) 的 AT 固件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#esp32-mini-1-esp32-u4wdh-at) 

- 7 [ADV 广播参数超过 32 字节之后应该如何设置?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#adv-32) 

- 8 [AT 支持 Wi-Fi 漫游功能吗?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#at-wi-fi) 

- 9 [使用 ESP-AT 发送 TCP 数据时，有时数据会混乱/部分丢失，应该如何处理？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#esp-at-tcp) 

- 10 [ESP32 进行 BLE OTA 时，使用 BLE 连接手机、UART 连接 MCU ，对 MCU 进行 OTA。手机设置 MTU 增大后，ESP32 与 MCU 端数据传输仍然很慢。可以从哪方面排查？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#esp32-ble-ota-ble-uart-mcu-mcu-ota-mtu-esp32-mcu) 

- 11 [使用 ESP32-C3 作为 Server 且 AT 固件版本为 v2.2.0.0 时，AT+CIPSERVERMAXCONN 指令允许建立的最大连接数是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#esp32-c3-server-at-v2-2-0-0-at-cipservermaxconn) 

- 12 [使用 release/v2.1.0.0 版本的 AT 固件，ESP32 最多支持保存多少个 BLE 设备的绑定配对信息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#release-v2-1-0-0-at-esp32-ble) 

- 13 [AT+BLEADVDATA 广播数据支持的最大长度为 31，如何支持更大的数据长度?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#at-bleadvdata-31) 

- 14 [WPA2 Enteprise 支持哪些认证方式呢 ?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#wpa2-enteprise) 

- 15 [AT+HTTPCPOST 有哪些使用示例?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#at-httpcpost) 

- 16 [是否有 AT+CIPRECVDATA 接收服务器端缓存数据示例?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#at-ciprecvdata) 

- 17 [使用 ESP32 的 AT 固件，发送 BLE 扫描命令，没有收到扫描应答包，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#esp32-at-ble) 

- 18 [使用 AT+BLEADVDATA 指令发广播包最大长度有限制吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#id6) 

- 19 [使用 ESP32 的 v2.2.0.0 版本的 AT 固件，AT+BLEGATTCWR 指令的 “length” 参数最大可以设置多大？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#esp32-v2-2-0-0-at-at-blegattcwr-length) 

- 20 [ESP32 使用 v2.2.0.0 版本的 AT 固件连接上 AP，重新复位上电后会自动连接 AP，如何取消这个设置？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#esp32-v2-2-0-0-at-ap-ap) 

- 21 [ESP32-AT 支持 PPP 吗?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#esp32-at-ppp) 

- 22 [AT 如何使能 Wi-Fi Debug ?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#at-wi-fi-debug) 

- 23 [使用 AT+SYSFLASH 指令更新证书应注意什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#at-sysflash) 

- 24 [AT+HTTPCPOST 指令中 content-type 默认类型是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#at-httpcpost-content-type) 

- 25 [AT+HTTPCLIENT 发送数据到服务器有长度限制吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#at-httpclient) 

- 26 [AT 支持 哪些 TLS 版本 ？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#at-tls) 

- 27 [如何存储 BLE 名称到 flash 中？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#ble-flash) 

- 28 [BLE 客户端如何使能 notify 和 indicate 功能？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#ble-notify-indicate) 

- 29 [ESP32 端作为 slave 时，MCU 端如何定义 json 格式的 MQTT 数据，字符串如何转义？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#esp32-slave-mcu-json-mqtt) 

- 30 [ESP8266-NONOS 版本的 AT 固件，默认使用的 AT 指令传输串口是哪个？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/at-application.html#esp8266-nonos-at-at) 

### 3.3 [Wi-Fi Mesh 应用框架](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html) 

- 1 [ESP-WIFI-MESH 能否批量 OTA？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp-wifi-mesh-ota) 

- 2 [ESP32 支持多少设备进行 ESP-WIFI-MESH 组网？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp32-esp-wifi-mesh) 

- 3 [ESP32 的 ESP-WIFI-MESH Router 模式与 No Router 模式有什么区别？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp32-esp-wifi-mesh-router-no-router) 

- 4 [ESP32 的 ESP-WIFI-MESH 能否在子设备搜索不到路由器信号时完成组网？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#id1) 

- 5 [ESP32 的 ESP-WIFI-MESH 是否可自动修复网络？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#id2) 

- 6 [使用 ESP32 的 ESP-WIFI-MESH，如何设置可以在没连接到 Wi-Fi 的情况下形成自组网？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp32-esp-wifi-mesh-wi-fi) 

- 7 [使用 ESP32 进行 ESP-WIFI-MESH 应用，在组网自动选举根节点时，是否可以指定局部模块进行选举？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#id5) 

- 8 [使用 ESP32 进行 ESP-WIFI-MESH 应用，在无路由场景下，多个根节点之间能互发消息吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#id6) 

- 9 [ESP-WIFI-MESH 可以批量 OTA 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#id7) 

- 10 [如何查询 ESP-WIFI-MESH APP 端源码？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp-wifi-mesh-app) 

- 11 [ESP-WIFI-MESH 是否有无路由方案完成自组网？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#id8) 

- 12 [利用 Mwifi 自动组网后，如何获得某个节点的所有潜在父节点的信号强度 (rssi)？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#mwifi-rssi) 

- 13 [在 esp-mdf 的 MESH 网络内部，节点之间的通信是基于什么协议？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp-mdf-mesh) 

- 14 [ESP-WIFI-MESH 可以将所有的节点都连接至路由上吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#id9) 

- 15 [ESP-WIFI-MESH 的 root 节点能否通过 4G 拨号实现联网？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp-wifi-mesh-root-4g) 

- 16 [esp_mesh_set_parent 函数成功连接后，断开 AP，该函数会不断发起重新连接，如何设置重新连接次数？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp-mesh-set-parent-ap) 

- 17 [设置按钮后报错：<code class="docutils literal notranslate"><span class="pre">phy_init:</span> <span class="pre">failed</span> <span class="pre">to</span> <span class="pre">load</span> <span class="pre">RF</span> <span class="pre">calibration</span> <span class="pre">data</span></code>。](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#phy-init-failed-to-load-rf-calibration-data) 

- 18 [如何暂停/恢复 Mwifi？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#mwifi) 

- 19 [ESP32-S 无路由 MESH 组网，APP 怎么连接 root 接口的 softAP？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp32-s-mesh-app-root-softap) 

- 20 [ESP-WIFI-MESH 能连到 AP，但不能连到 AP 上的 TCP SERVER？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp-wifi-mesh-ap-ap-tcp-server) 

- 21 [Mwifi 例程怎么修改网络的 AP 连接和最大层数？通信时的最大带宽和延时是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#mwifi-ap) 

- 22 [如何获得实时的传感器返回值？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#id10) 

- 23 [新节点可能已经安装在设备中，且该设备已经安装在距离 ROOT 节点较远的位置，请问该节点如何加入 ESP-WIFI-MESH 网络？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#root-esp-wifi-mesh) 

- 24 [ESP-WIFI-MESH App 源码是否开放？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#id12) 

- 25 [Wi-Fi Mesh 数据传送最大的包为多少 Bytes？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#wi-fi-mesh-bytes) 

- 26 [ESP32 的 Wi-Fi Mesh 支持 No Router 自组网吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp32-wi-fi-mesh-no-router) 

- 27 [ESP32 使用 Wi-Fi Mesh 时允许的最大节点层数是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp32-wi-fi-mesh) 

- 28 [使用 ESP32 开发板测试 esp-mdf/examples/function_demo/mwifi/router 例程，ESP32 连接路由器后，在路由器连接端显示的设备名称为 “espressif”，如何修改此名称？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp32-esp-mdf-examples-function-demo-mwifi-router-esp32-espressif) 

- 29 [Wi-Fi Mesh 可以通过 TCP Server 给特定节点发送消息吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#wi-fi-mesh-tcp-server) 

- 30 [在 ESP32 Wi-Fi Mesh 网络运行过程中，若根 (Root) 节点丢失，系统会反馈什么事件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp32-wi-fi-mesh-root) 

- 31 [使用 ESP32 进行 Wi-Fi Mesh 应用开发，目前使用的是 esp_mesh_send() 函数，发现服务器没有接收到任何数据。如何将数据从叶节点 (leaf node) 传输到外部服务器？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp32-wi-fi-mesh-esp-mesh-send-leaf-node) 

- 32 [ESP-MESH 设备组网之后如何做 OTA 升级？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp-mesh-ota) 

- 33 [是否有 ESP-MESH 灯参考设计？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp-mesh) 

- 34 [ESP-MESH 节点不做任何配置，默认是什么模式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#id13) 

- 35 [ESP-MESH 启动时开启 AP+STA 模式，手机可以搜索到 AP 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp-mesh-ap-sta-ap) 

- 36 [设备已经组网完成，新增设备是否需要全部重新扫描？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#id14) 

- 37 [ESP32 作为主设备对多个从设备进行时间同步，是否可以满足误差在 2 ms 内的需求？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp32-2-ms) 

- 38 [ESP-MESH 中如何获取节点类型？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#id15) 

- 39 [ESP-Mesh 根节点通过 ethernet 向服务发消息示例？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/wifi-mesh-development-framework.html#esp-mesh-ethernet) 

### 3.4 [BLE Mesh 应用框架](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html) 

- 1 [手机 App 首先配置的节点的单播地址是不是固定的？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#app) 

- 2 [配网过程中，认证设备共有多少种方法？提供的范例中 provided examples 使用了什么方法？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#provided-examples) 

- 3 [配置入网前，未配网设备的广播包可以携带哪些信息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id1) 

- 4 [ESP-BLE-MESH 如何打印数据包？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#esp-ble-mesh) 

- 5 [Device UUID 可以用于设备识别吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#device-uuid) 

- 6 [如何知道当前 Provisioner 正在配网哪个未配网设备？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#provisioner) 

- 7 [Provisioner 如何通过获取的 Composition Data 进一步配置节点？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#provisioner-composition-data) 

- 8 [节点可以自己添加相应的配置吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id2) 

- 9 [Provisioner 如何通过分组的方式控制节点？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id3) 

- 10 [Provisioner 如何知道网络中的某个设备是否离线？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id4) 

- 11 [Provisioner 如何将节点添加至多个子网？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id5) 

- 12 [为什么 APP 中显示的节点地址的数量比现有的节点地址更多？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id6) 

- 13 [在 EspBleMesh App 中输入的 <code class="docutils literal notranslate"><span class="pre">count</span></code> 值有什么用途？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#espblemesh-app-count) 

- 14 [运行以下示例 fast_prov_server 的节点的 Configuration Client Model 何时开始工作？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#fast-prov-server-configuration-client-model) 

- 15 [Temporary Provisioner 功能会一直处于使能的状态吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#temporary-provisioner) 

- 16 [BLE MESH Log <code class="docutils literal notranslate"><span class="pre">ran</span> <span class="pre">out</span> <span class="pre">of</span> <span class="pre">retransmit</span> <span class="pre">attempts</span></code> 代表什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#ble-mesh-log-ran-out-of-retransmit-attempts) 

- 17 [BLE Mesh log <code class="docutils literal notranslate"><span class="pre">Duplicate</span> <span class="pre">found</span> <span class="pre">in</span> <span class="pre">Network</span> <span class="pre">Message</span> <span class="pre">Cache</span></code> 代表什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#ble-mesh-log-duplicate-found-in-network-message-cache) 

- 18 [BLE Mesh log <code class="docutils literal notranslate"><span class="pre">Incomplete</span> <span class="pre">timer</span> <span class="pre">expired</span></code> 代表什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#ble-mesh-log-incomplete-timer-expired) 

- 19 [BLE Mesh log <code class="docutils literal notranslate"><span class="pre">No</span> <span class="pre">free</span> <span class="pre">slots</span> <span class="pre">for</span> <span class="pre">new</span> <span class="pre">incoming</span> <span class="pre">segmented</span> <span class="pre">messages</span></code> 代表什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#ble-mesh-log-no-free-slots-for-new-incoming-segmented-messages) 

- 20 [BLE Mesh log <code class="docutils literal notranslate"><span class="pre">No</span> <span class="pre">matching</span> <span class="pre">TX</span> <span class="pre">context</span> <span class="pre">for</span> <span class="pre">ack</span></code> 代表什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#ble-mesh-log-no-matching-tx-context-for-ack) 

- 21 [BLE Mesh log <code class="docutils literal notranslate"><span class="pre">Model</span> <span class="pre">not</span> <span class="pre">bound</span> <span class="pre">to</span> <span class="pre">AppKey</span> <span class="pre">0x0000</span></code> 代表什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#ble-mesh-log-model-not-bound-to-appkey-0x0000) 

- 22 [BLE Mesh log <code class="docutils literal notranslate"><span class="pre">Busy</span> <span class="pre">sending</span> <span class="pre">message</span> <span class="pre">to</span> <span class="pre">DST</span> <span class="pre">xxxx</span></code> 代表什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#ble-mesh-log-busy-sending-message-to-dst-xxxx) 

- 23 [为什么会出现 EspBleMesh App 在快速配网期间长时间等待的情况？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#espblemesh-app) 

- 24 [Provisoner 如何控制节点的服务器模型？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#provisoner) 

- 25 [设备通信必须要网关吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id7) 

- 26 [Provisioner 删除网络中的节点时，需要进行哪些操作？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id8) 

- 27 [在密钥更新的过程中，Provisioner 如何更新节点的网络密钥？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id10) 

- 28 [Provisioner 如何管理 mesh 网络中的节点？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#provisioner-mesh) 

- 29 [Provisioner 想要控制节点的服务器模型时需要什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id12) 

- 30 [什么时候应该使能节点的 Relay 功能？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#relay) 

- 31 [节点包含什么样的模型？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id13) 

- 32 [每个模型对应的消息格式是不是固定的？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id14) 

- 33 [节点的模型可以使用哪些函数发送消息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id15) 

- 34 [如何实现消息传输不丢包？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id16) 

- 35 [如何发送无应答的消息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id17) 

- 36 [发送不分包消息时，最多可携带多少有效字节？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id18) 

- 37 [什么时候应该使能节点的 Proxy 功能？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#proxy) 

- 38 [如何使用代理过滤器？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id19) 

- 39 [如何实现将节点自检的信息发送出来？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id20) 

- 40 [Relay 节点什么时候可以中继消息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id21) 

- 41 [如果一条消息分成几段，那么其他 Relay 节点是接收到一段消息就中继还是等接收到完整的数据包才中继？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id22) 

- 42 [设备断电后上电，如何能继续在网络中进行通讯？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id23) 

- 43 [使用 Low Power 功能降低功耗的原理是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#low-power) 

- 44 [节点间如何传输消息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id24) 

- 45 [何时使用 IV Update 更新程序？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#iv-update) 

- 46 [为什么需要快速配网？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id25) 

- 47 [如何启用 IV Update 更新程序？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id26) 

- 48 [ESP-BLE-MESH 回调函数如何分类？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id27) 

- 49 [未配网设备加入 ESP-BLE-MESH 网络的流程是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id28) 

- 50 [Provisioner 的地址是否可以作为节点上报状态消息的目的地址？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id29) 

- 51 [如果 Provisioner 想要改变节点状态，其需满足什么条件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id30) 

- 52 [Provisioner 的单播地址是不是固定的？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id31) 

- 53 [如何使用网络密钥和应用密钥？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id32) 

- 54 [是否可以采用固定的网络密钥或应用密钥？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id33) 

- 55 [如何清除 ESP32 BLE node 的组网信息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#esp32-ble-node) 

- 56 [如何删除某个 node 的组网信息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#node) 

- 57 [如果 Node 断电了，下次上电是否还要用手机 APP 重新组网？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#node-app) 

- 58 [1号板子做 provisioner，2,3,4号板子做 Node 。组网成功后，如果1号板子掉电了，重新上电后还能否加入到这个 mesh 网络中？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#provisioner-2-3-4-node-1-mesh) 

- 59 [BLE_MESH 中，某个 Node 如果掉线了，要如何知道？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#ble-mesh-node) 

- 60 [BLE_MESH 节点间如何实现以字符串的形式通信？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id34) 

- 61 [配置ble mesh保存节点信息时初始化partition失败: <code class="docutils literal notranslate"><span class="pre">BLE_MESH:</span> <span class="pre">Failed</span> <span class="pre">to</span> <span class="pre">init</span> <span class="pre">mesh</span> <span class="pre">partition,</span> <span class="pre">name</span> <span class="pre">ble_mesh,</span> <span class="pre">err</span> <span class="pre">261</span></code>](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#ble-meshpartition-ble-mesh-failed-to-init-mesh-partition-name-ble-mesh-err-261) 

- 62 [请问如何在 provisioner 的 demo 中 添加 health_mode？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#provisioner-demo-health-mode) 

- 63 [ble_mesh_fast_prov_client 当设备 provisioner 和手机当 provisioner 有什么不一样？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#ble-mesh-fast-prov-client-provisioner-provisioner) 

- 64 [有什么工具和办法可以查看 ble_mesh node 之间的加密消息吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id35) 

- 65 [app key 是否是厂家可以自己设置？ Unicast address 和 app key 是否有某种关联？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#app-key-unicast-address-app-key) 

- 66 [如果一个 Node 突然掉线，那么通过 Health model 监测消息的机制，是整个 mesh 网络都要轮询的发送 Heartbeat 消息吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#node-health-model-mesh-heartbeat) 

- 67 [主 Node（代理节点） -&gt; 从 Node互相发送消息，用client-server模型可以吗？是否有提供demo来完成？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#node-node-client-server-demo) 

- 68 [在 NRF 的手机 app 里，右下角 “Setting” 里有个 “Network Key”，可以自由更改，这个修改的是指哪个 network key 呢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#nrf-app-setting-network-key-network-key) 

- 69 [设备如何加入 BLE-Mesh 网络？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#id36) 

- 70 [Bluetooth® LE (BLE) Mesh 数据传送最大的包是多少 Bytes？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#bluetooth-le-ble-mesh-bytes) 

- 71 [能否提供通过 ESP32 BLE-Mesh 组网的例程？配置组网的 APP 可以使用什么软件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#esp32-ble-mesh-app) 

- 72 [在 BLE-MESH 中，未配网设备默认的名称是 ESP-BLE-MESH，这个名称在哪里可以修改？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#ble-mesh-esp-ble-mesh) 

- 73 [ESP32 的 BLE-MESH 应用可以连接多少个节点设备？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ble-mesh-development-framework.html#esp32-ble-mesh) 

### 3.5 [音频应用框架](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html) 

- 1 [使用 ESP32-Korvo-DU1906 开发板必须用百度云吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp32-korvo-du1906) 

- 2 [乐鑫官网给出的网络电话例程是否支持 RTP？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#rtp) 

- 3 [ESP-ADF 中 RTP 协议是否开源？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp-adf-rtp) 

- 4 [ESP-ADF 例程能否实现蓝牙耳机的音量调节功能？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp-adf) 

- 5 [我想在 ESP32-LyraT 的 I2C 接一个传感器使用，请问有如何读取 I2C 设备数据的例程吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp32-lyrat-i2c-i2c) 

- 6 [如何输出 32bit 的 I2S 音频数据？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#bit-i2s) 

- 7 [请问为何用 ESP-ADF 和 ESP-IDF v4.1 编译 example/get-started/play-pm3 时总是报错？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp-adf-esp-idf-v4-1-example-get-started-play-pm3) 

- 8 [请问官方有没有可以支持 ESP-IDF v4.4 的 ESP-ADF 版本？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp-idf-v4-4-esp-adf) 

- 9 [加入 DuerOS 是否会将 esp32-lyrat 开发板的录音功能全程占用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#dueros-esp32-lyrat) 

- 10 [ESP32-LyraT V4.3 不支持 dueros 吗？烧进去 dueros 固件，机器一直重启？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp32-lyrat-v4-3-dueros-dueros) 

- 11 [ESP-ADF 支持语音识别关键词自定义开发吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#id4) 

- 12 [ESP-ADF 是否支持 ESP32-LyraTD-MSC V2.1 开发板跑 Alexa 例程？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp-adf-esp32-lyratd-msc-v2-1-alexa) 

- 13 [ESP32 关于语音识别方面，要能本地化，能否推荐相应的开发板？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp32) 

- 14 [ESP32 是否有同时支持 MIC 和 AUX 拾音的开发板？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp32-mic-aux) 

- 15 [如何利用 ESP32-LyraT 开发板实现通话功能？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp32-lyrat) 

- 16 [ESP32 系列音频开发板支持多大功率的扬声器？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#id5) 

- 17 [Alexa solution 对环境噪声是否有一定的要求？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#alexa-solution) 

- 18 [ESP32 的 AI 开发板上有 AUX 输入，MIC 就无法拾音了吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp32-ai-aux-mic) 

- 19 [使用 ESP32-WROVER-B 模组 + ES8311 设计音频开发板，MCLK 时钟可选择哪些管脚？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp32-wrover-b-es8311-mclk) 

- 20 [ESP32-WROVER-E 模组使用一路 I2S 是否可实现同时播音和录音？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp32-wrover-e-i2s) 

- 21 [乐鑫模块是否支持 Spotify Connect？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#spotify-connect) 

- 22 [ESP32-Korvo-DU1906 开发板运行 korvo_du1906 示例重启，错误提示如下：Guru Meditation Error: Core  0 panic’ed (IllegalInstruction). Exception was unhandled，如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp32-korvo-du1906-korvo-du1906-guru-meditation-error-core-0-panic-ed-illegalinstruction-exception-was-unhandled) 

- 23 [ESP-DSP fft 可以运行 4096、8192 以及更多采样吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#esp-dsp-fft-40968192) 

- 24 [ESP32 如何连接麦克风？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#id7) 

- 25 [ESP32 是否支持模拟音频或是数字音频输出？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/audio-development-framework.html#id8) 

### 3.6 [第三方云服务](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/third-party-cloud-service.html) 

- 1 [ESP32 如何对接天猫精灵，是否有相应的资料？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/third-party-cloud-service.html#esp32) 

- 2 [esp-aliyun 与 esp-ali-smartliving 的区别 ？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/third-party-cloud-service.html#esp-aliyun-esp-ali-smartliving) 

- 3 [使用乐鑫的产品连接乐鑫云平台，遇到问题如何提问与反馈？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/third-party-cloud-service.html#id3) 

- 4 [ESP32 与 ESP8266 可以连接 Alexa 或者 Google home 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/third-party-cloud-service.html#esp32-esp8266-alexa-google-home) 

- 5 [ESP32 + 以太网 + MQTT 方式接入阿里云，应该怎么做？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/third-party-cloud-service.html#esp32-mqtt) 

### 3.7 [ESP RainMaker 云服务](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html) 

- 1 [ESP RainMaker 对接了哪些语音平台? 支持哪些语音指令？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#id5) 

- 2 [RainMaker 设备的证书如何获取？是否有管理后台？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#id6) 

- 3 [ESP RainMaker 固件侧代码开发与腾讯云、阿里云的开发模式有什么不同？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#id10) 

- 4 [ESP RainMaker 公有云与 ESP RainMaker 私有云有什么区别？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#esp-rainmaker-esp-rainmaker) 

- 5 [Nova Home 跟 ESP RainMaker 有什么关系？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#nova-home-esp-rainmaker) 

- 6 [除 Github 外是否有其他途径拉取 ESP RainMaker 源码？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#github-esp-rainmaker) 

- 7 [CLI 工具如何使用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#cli) 

- 8 [ESP RainMaker App 执行 Claiming 时出现了错误该如何处理？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#esp-rainmaker-app-claiming) 

- 9 [ESP RainMaker 中节点、节点属性、设备、设备属性、服务、参数都是什么？有什么用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#id17) 

- 10 [ESP RainMaker 是否支持设备与设备之间的联动？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#id18) 

- 11 [ESP RainMaker 是否支持 App 端的消息推送？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#esp-rainmaker-app) 

- 12 [ESP RainMaker 是否支持带时间戳数据的上报及后续的分析？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#id19) 

- 13 [ESP RainMaker App 与 Nova Home App 可以从哪获取？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#esp-rainmaker-app-nova-home-app) 

- 14 [ESP RainMaker 中节点配置信息有什么用？与参数信息的区别是什么？如何查看？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#id23) 

- 15 [ESP RainMaker 中设备最多能上报多大的消息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#id25) 

- 16 [ESP RainMaker App 中显示设备离线总是很慢，能否加快？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#id27) 

- 17 [ESP RainMaker 方案适配了哪些芯片？用哪个 IDF 版本编译？是否支持其他平台的芯片？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#esp-rainmaker-idf) 

- 18 [ESP RainMaker 方案中 Claiming 有 3 种形式，区别在哪？该如何选择？能否在私有部署使用中使用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#esp-rainmaker-claiming-3) 

- 19 [ESP RainMaker 支持哪些配网方式？这些配网如何实现？能否修改添加自己的配网逻辑？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#id32) 

- 20 [ESP RainMaker App 在配网时有时会弹出配对选项，如何取消？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#id33) 

- 21 [ESP RainMaker 是否支持本地控制？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#id34) 

- 22 [使用 ESP RainMaker Topic 方式进行 OTA 时，有时会报 <cite>! The certificate is not correctly signed by the trusted CA</cite>，这该如何处理 ？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#esp-rainmaker-topic-ota-the-certificate-is-not-correctly-signed-by-the-trusted-ca) 

- 23 [Swagger 上提供的 RESTful API 可以在线调试吗?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#swagger-restful-api) 

- 24 [ESP RainMaker App 中的 UI 是如何确定的? 如何自定义呢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/esp-rainmaker-cloud-service.html#esp-rainmaker-app-ui) 

### 3.8 [社区软件平台](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/community-sw-and-platforms.html) 

### 3.9 [苹果应用](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ios-application.html) 

- 1 [阿里飞燕平台 SDk 为何报错找不到 #import &lt;IMLDeviceCenter/IMLDeviceCenter.h&gt; 头文件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ios-application.html#sdk-import-imldevicecenter-imldevicecenter-h) 

- 2 [iOS 13.0 及以上版本如何获取 Wi-Fi 信息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ios-application.html#ios-13-0-wi-fi) 

- 3 [iOS 14.0 如何增加本地网络权限？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ios-application.html#ios-14-0) 

- 4 [AWS 如何生成 .p12 证书？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ios-application.html#aws-p12) 

- 5 [如何获取 AWS SDK 自带登录注册验证码？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ios-application.html#aws-sdk) 

- 6 [APP 如何在后台扫描蓝牙（两种方式）？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ios-application.html#app) 

- 7 [如何解决 iOS 14.5 UDP 广播 sendto 返回 -1 的错误？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/ios-application.html#ios-14-5-udp-sendto-1) 

### 3.10 [安卓应用](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/android-application.html) 

- 1 [为什么扫描 Wi-Fi 和蓝牙信号需要位置权限？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/android-application.html#wi-fi) 

- 2 [APP 需要继承第三方库中的 Application 类，但如需同时继承 MultiDexApplication 怎么办？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/android-application.html#app-application-multidexapplication) 

- 3 [APP 发送 http 请求报错是为什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/android-application.html#app-http) 

- 4 [怎么把 APP 的签名文件迁移到 pkcs12？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/android-application.html#app-pkcs12) 

- 5 [在不安装 Android Studio 的情况下怎么查看 APP 的日志输出？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/android-application.html#android-studio-app) 

- 6 [如何在 Module 的 BuildConfig 中添加模块版本信息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/android-application.html#module-buildconfig) 

### 3.11 [摄像头应用](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/camera-application.html) 

- 1 [摄像头输出图像都有什么格式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/camera-application.html#id3) 

- 2 [摄像头支持哪些参数调整？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/camera-application.html#id4) 

- 3 [摄像头中 MCLK 和 PCLK 区别及关系？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/camera-application.html#mclk-pclk) 

- 4 [摄像头的 PCLK 是不是越高越好？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/camera-application.html#pclk) 

- 5 [ESP32 系列芯片支持 MIPI 接口吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/camera-application.html#esp32-mipi) 

- 6 [ESP32 系列芯片支持 USB2.0 接口吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/camera-application.html#esp32-usb2-0) 

- 7 [摄像头中 YUV/RGB 的传输速度为何会比 JPEG 慢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/camera-application.html#yuv-rgb-jpeg) 

- 8 [摄像头应用中影响帧率的因素？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/camera-application.html#id5) 

- 9 [摄像头运行失败如何排查？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/camera-application.html#id6) 

- 10 [ESP32 支持传输视频流吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/camera-application.html#id7) 

- 11 [ESP-EYE 的出厂固件在哪里？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/camera-application.html#esp-eye) 

- 12 [Camera 方案相关的示例在哪里？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/application-solution/camera-application.html#camera) 


-------------------------------------------------------
## 4 [软件平台](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/index.html) 

### 4.1 [蓝牙](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html) 

- 1 [ESP32 可以支持 Bluetooth® LE 5.0 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-bluetooth-le-5-0) 

- 2 [为什么 Bluetooth® LE 开始广播后，有些手机扫描不到？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#bluetooth-le) 

- 3 [ESP32 能否使用蓝牙进行 OTA？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-ota) 

- 4 [ESP32 的蓝牙双模如何共存及使用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32) 

- 5 [ESP32 的 Bluetooth® LE 吞吐量是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-bluetooth-le) 

- 6 [ESP32 是否支持 BT4.2 DLE (Data Length Extension)？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-bt4-2-dle-data-length-extension) 

- 7 [ESP32 的蓝⽛和 Wi-Fi 如何共存？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-wi-fi) 

- 8 [ESP32 蓝牙的兼容性测试报告如何获取？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id2) 

- 9 [ESP32 蓝牙的发射功率是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id3) 

- 10 [ESP32 可以实现 Wi-Fi 和 Bluetooth® LE 桥接的功能吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-wi-fi-bluetooth-le) 

- 11 [ESP32 的 Bluetooth® LE 工作电流是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id4) 

- 12 [ESP32 支持哪些 Bluetooth® LE Profile？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-bluetooth-le-profile) 

- 13 [如何使用 ESP32 蓝牙连接手机播放音乐？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id5) 

- 14 [ESP32 的 SPP 性能如何？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-spp) 

- 15 [ESP32 的 Bluetooth® LE 传输速率最大为多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id6) 

- 16 [ESP32 Bluetooth® LE 如何进入 Light-sleep 模式呢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-bluetooth-le-light-sleep) 

- 17 [选择 ESP32 芯片实现蓝牙配网的方式，是否有文档可以提供参考？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id7) 

- 18 [ESP32 经典蓝牙 SPP 的传输速率能达到多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id8) 

- 19 [ESP32 的蓝牙是否兼容 Bluetooth® ver2.1 + EDR 协议？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-bluetooth-ver2-1-edr) 

- 20 [ESP32 支持多少蓝牙客户端连接？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id10) 

- 21 [ESP32 如何获取蓝牙设备的 MAC 地址？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-mac) 

- 22 [ESP32 SDK 中默认的蓝牙的发射功率是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-sdk) 

- 23 [ESP32 Wi-Fi Smartconfig 配网和 Bluetooth® LE Mesh 可以同时使用吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-wi-fi-smartconfig-bluetooth-le-mesh) 

- 24 [ESP32 的经典蓝牙工作电流是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id11) 

- 25 [ESP32 如何修改蓝牙的发射功率？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id12) 

- 26 [ESP32 的 Bluetooth® LE 蓝牙配网兼容性如何？是否开源？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id13) 

- 27 [ESP32 运行 bt_spp_acceptor 例程时， IOS 设备无法扫描到 ESP32 设备是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-bt-spp-acceptor-ios-esp32) 

- 28 [ESP32 Bluetooth® LE/Bluetooth® Secure Simple Pairing (SSP) 与 legacy pairing 安全性对比？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-bluetooth-le-bluetooth-secure-simple-pairing-ssp-legacy-pairing) 

- 29 [ESP32 Bluetooth® LE MTU 大小如何确定？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-bluetooth-le-mtu) 

- 30 [ESP32 Bluetooth® LE 模式下广播数据时遇到 “W (17370) BT_BTM: data exceed max adv packet length” 如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-bluetooth-le-w-17370-bt-btm-data-exceed-max-adv-packet-length) 

- 31 [ESP32 Bluetooth® LE 能否同时支持主从模式，作 gatt server 的同时，也可作为 gatt client 接收其他设备的广播数据？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-bluetooth-le-gatt-server-gatt-client) 

- 32 [ESP32 的 Bluetooth® LE 连接数 6 个以上会有哪些风险？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-bluetooth-le-6) 

- 33 [使用 ESP32 设备作为 Bluetooth® LE 主机，最大支持多少台从机设备进行连接？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id14) 

- 34 [ESP32 如何通过 Bluetooth® BR/EDR 传文件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-bluetooth-br-edr) 

- 35 [ESP32 下载 ESP_SPP_SERVER 例程，如何修改蓝牙设备名称？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-esp-spp-server) 

- 36 [ESP32 下载 BluFi 例程进行配网，若使用 EspBluFi APP 在配网过程配置了一个错误的 Wi-Fi 从而无法连接，此时从 APP 端向设备端发送“扫描”命令后就会导致设备重启，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-blufi-espblufi-app-wi-fi-app) 

- 37 [使用 ESP32，如何指定 BLE 连接/发送在 core 0 上运行？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-ble-core-0) 

- 38 [ESP32 设置中文蓝牙设备名称会异常显示乱码，原因是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id15) 

- 39 [使用 ESP32 在蓝牙通道上传分包时，一包最大传输数据长度为 253（MTU 设置为 263），导致在传输大量数据包进行多包读取时传输较慢。请问是否有 BluFi 扩展协议，可支持一包传输较大长度的数据，或者有其他解决方案可提高传输速率吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-253-mtu-263-blufi) 

- 40 [ESP32 经典蓝牙支持哪些 Profile？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-profile) 

- 41 [ESP32-C3 Bluetooth® LE (BLE) 稳定连接的数目可以达到多少个？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-c3-bluetooth-le-ble) 

- 42 [BLE 中如何修改广播的时间间隔？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#ble) 

- 43 [ESP32 经典蓝牙配对时如何使手机端输入 PIN 码？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-pin) 

- 44 [ESP32 蓝牙占用多少内存？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id16) 

- 45 [ESP32 使用 gattc_gatts_coex.c 例程测试 BLE 多连接，在 <code class="docutils literal notranslate"><span class="pre">menuconfi</span></code> 中将 <code class="docutils literal notranslate"><span class="pre">BLE</span> <span class="pre">Max</span> <span class="pre">connection</span></code> 配置选项设置为 “5” ，但实际只能连 4 个设备，连接第 5 个设备的时候会报错，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-gattc-gatts-coex-c-ble-menuconfi-ble-max-connection-5-4-5) 

- 46 [ESP32-C3 BLE 同时支持主从模式吗？主、从模式连接数分别是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-c3-ble) 

- 47 [ESP32 经典蓝牙的 MTU Size 最大可设多大呢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-mtu-size) 

- 48 [Wi-Fi 和 蓝牙共存时，频繁通信出现 ELxXX error（比如 ELx200）如何解决?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#wi-fi-elxxx-error-elx200) 

- 49 [BLE 如何抓包？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id17) 

- 50 [使用 ESP32 开发板，测试好几个版本的 ESP-IDF 下的 BluFi 例程进行配网，点击配网之后都会打印如下报错，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-esp-idf-blufi) 

- 51 [使用 ESP32，请问蓝牙能否使用 light-sleep 模式，并在 light-sleep 模式下保持蓝牙连接？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-light-sleep-light-sleep) 

- 52 [如何修改 ESP32 的蓝牙广播名称？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id18) 

- 53 [BLE 5.0 广播设置为 legacy 模式时支持最大广播长度为多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#ble-5-0-legacy) 

- 54 [BLE 广播包如何设置为不可连接包?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id19) 

- 55 [怎样通过串口给 ESP32-WROOM-32D 模块直接发送蓝牙 HCI 命令?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-wroom-32d-hci) 

- 56 [ESP32 如何手动重置 BLE mesh 设备（不通过 mobile provisioning app 或 provisioning device）？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-ble-mesh-mobile-provisioning-app-provisioning-device) 

- 57 [ESP32 是否支持 A2DP 发送音频？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-a2dp) 

- 58 [ESP32 Bluetooth LE 白名单最多支持多少个设备？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#id20) 

- 59 [ESP32 低功耗蓝牙可以使用 PSRAM 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ble-bt.html#esp32-psram) 

### 4.2 [以太网](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ethernet.html) 

- 1 [ESP32 外接 LAN8720，GPIO0 对其提供 CLK，Ethernet 例程初始化出错。如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ethernet.html#esp32-lan8720-gpio0-clk-ethernet) 

- 2 [使用 ESP-IDF 中的 Ethernet 示例时，出现错误代码 “Timed out waiting for PHY register 0x3 to have value 0xc0f0 (mask 0xfff0). Current value 0xffff”，请问该如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ethernet.html#esp-idf-ethernet-timed-out-waiting-for-phy-register-0x3-to-have-value-0xc0f0-mask-0xfff0-current-value-0xffff) 

- 3 [使用 ESP-IDF v4.1，ESP32 Ethernet 如何设置静态 IP？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ethernet.html#esp-idf-v4-1-esp32-ethernet-ip) 

- 4 [ESP32-Ethernet-Kit 开发板模组替换成 ESP32-WROOM-32D 以太网功能是否存在影响？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ethernet.html#esp32-ethernet-kit-esp32-wroom-32d) 

- 5 [使用 ESP32 设计自行开发以太网的板子，下载官方 esp-idf/examples/ethernet 例程，报错如下，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ethernet.html#esp32-esp-idf-examples-ethernet) 

- 6 [ESP32 以太网支持 MII 接口吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ethernet.html#esp32-mii) 

- 7 [ESP32-S2 是否可以外接以太网？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/ethernet.html#esp32-s2) 

### 4.3 [共存](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/coexistence.html) 

- 1 [Wi-Fi 和 ESP-BLE-MESH 共存时，为什么 Wi-Fi 吞吐量很低？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/coexistence.html#wi-fi-esp-ble-mesh-wi-fi) 

- 2 [ESP32 支持 16 MB 的 External Flash 和 8 MB 的 External PSRAM 共存吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/coexistence.html#esp32-16-mb-external-flash-8-mb-external-psram) 

- 3 [ESP32 的 ESP-WIFI-MESH 和 Bluetooth® LE Mesh 可以同时支持吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/coexistence.html#esp32-esp-wifi-mesh-bluetooth-le-mesh) 

- 4 [ESP32 蓝牙和 Wi-Fi 能否同时使用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/coexistence.html#esp32-wi-fi) 

- 5 [Wi-Fi、Bluetooth® LE 和 A2DP Sink 共存，进入 Bluetooth LE 扫描的时候音频数据接收会丢失、卡顿。怎么解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/coexistence.html#wi-fibluetooth-le-a2dp-sink-bluetooth-le) 

- 6 [ESP32 的网口 (LAN8720) 与 Wi-Fi (Wifi-AP) 能否共存？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/coexistence.html#esp32-lan8720-wi-fi-wifi-ap) 

- 7 [以太网 和 Wi-Fi 并存时，优先以太网传输数据吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/coexistence.html#id3) 

- 8 [BLE adverting (Connectable) + iBeacon sending(advertising) 可以共存吗？？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/coexistence.html#ble-adverting-connectable-ibeacon-sending-advertising) 

### 4.4 [外设](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/index.html) 

#### 4.5.1  [模拟数字转换器 (ADC)](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html) 

- 1 [ESP8266 如何获取 ADC 寄存器位图信息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html#id1) 

- 2 [ESP32 ADC 有⼏个通道？采样率和有效位数是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html#esp32-adc) 

- 3 [使用 ESP8266 调用 <code class="docutils literal notranslate"><span class="pre">adc_read_fast()</span></code> API 会导致 Wi-Fi 断连吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html#esp8266-adc-read-fast-api-wi-fi) 

- 4 [悬空 ADC 引脚，打印出 VDD3P3 的值为 65535，那么 VDD3P3 的电压就是 65535/1024 ≈ 63 V。这个电压值不符，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html#adc-vdd3p3-65535-vdd3p3-65535-1024-63-v) 

- 5 [ESP32 ADC 的输入电阻是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html#id3) 

- 6 [使用 ESP32 的 ADC 来检测电源电压，是否需要进行分压？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html#id4) 

- 7 [ESP32 芯片 ADC DMA 模式最高支持多大的采样频率？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html#esp32-adc-dma) 

- 8 [使用 ESP32，在 <code class="docutils literal notranslate"><span class="pre">esp_wifi_start()</span></code> 和 <code class="docutils literal notranslate"><span class="pre">esp_wifi_stop()</span></code> 之间读取 <code class="docutils literal notranslate"><span class="pre">adc2_get_raw()</span></code> 操作失败，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html#esp32-esp-wifi-start-esp-wifi-stop-adc2-get-raw) 

- 9 [ESP32 是否支持 ADC2 与蓝牙同时使用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html#esp32-adc2) 

- 10 [ESP32-S2 芯片 ADC DMA 模式支持的采样率范围是多大？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html#esp32-s2-adc-dma) 

- 11 [ESP32 的 ADC 支持多通道同时采样吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html#id5) 

- 12 [使用 ESP32-WROVER-B 模组，ESP-IDF 为 release/v4.2 版本，当 GPIO 设置为 ADC 接口后，在不进行硬件重启的情况下，再将 GPIO 设置为其他 IO 模式且其他 IO 模式不生效后，此 GPIO 无反应，请问如何释放对应的 GPIO 模式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html#esp32-wrover-b-esp-idf-release-v4-2-gpio-adc-gpio-io-io-gpio-gpio) 

- 13 [ESP32 芯片的 ADC 之间的测量误差是多大？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/adc.html#id6) 

#### 4.5.2  [数字模拟转换器 (DAC)](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/dac.html) 

#### 4.5.3  [GPIO &amp; RTC GPIO](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/gpio.html) 

- 1 [ESP8266 部分 GPIO 出现高电平的原因是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/gpio.html#esp8266-gpio) 

- 2 [ESP32 是否可以关闭线程调度使用一个单独的 CPU 以实现 GPIO 实时控制？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/gpio.html#esp32-cpu-gpio) 

- 3 [ESP32 GPIO 电平翻转速度是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/gpio.html#esp32-gpio) 

- 4 [ESP32 当⼀些 RTC 外设的电源打开时（SARADC1、SARADC2、AMP、HALL 传感器），GPIO36 和 GPIO39 的数字输⼊会被拉低约 80 ns，如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/gpio.html#esp32-rtc-saradc1saradc2amphall-gpio36-gpio39-80-ns) 

- 5 [ESP32 如果多个 GPIO 管脚配置了沿中断，则硬件可能⽆法正确触发中断。如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/gpio.html#id3) 

- 6 [使用 ESP-WROOM-02D 模组，GPIO0、GPIO15、GPIO1 和 GPIO3 是否可作为普通 GPIO 使用?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/gpio.html#esp-wroom-02d-gpio0gpio15gpio1-gpio3-gpio) 

- 7 [ESP32-C3 系列芯片将 GPIO19 配置成输入下拉时，读取该 IO 口状态依旧显示高电平，但配置 ESP32-C3 的其他管脚或者其他芯片的管脚为输入下拉时，均正常显示为低电平？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/gpio.html#esp32-c3-gpio19-io-esp32-c3) 

- 8 [使用 ESP-IDF release/v4.2 版本的 SDK，ESP32 如何设置单个 GPIO 同时作为输入/输出模式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/gpio.html#esp-idf-release-v4-2-sdk-esp32-gpio) 

#### 4.5.4  [I2C 驱动程序](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/i2c.html) 

- 1 [ESP8266 I2C 是软件模拟的吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/i2c.html#id1) 

#### 4.5.5  [集成电路内置音频总线 (I2S)](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/i2s.html) 

#### 4.5.6  [LCD](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/lcd.html) 

- 1 [ESP32 LCD 最大可以支持多大的分辨率？相应的帧率是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/lcd.html#esp32-lcd) 

- 2 [使用 ESP32-S3 测试 <a class="reference external" href="https://github.com/espressif/esp-iot-solution/tree/master/examples/hmi/lvgl_example">LVGL</a> 例程，请问目前已经适配了哪些型号的触摸屏？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/lcd.html#esp32-s3-lvgl) 

#### 4.5.7  [LED PWM 控制器 (LEDC)](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/ledc.html) 

- 1 [ESP32 GPIO 管脚输出 PWM 存在限制吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/ledc.html#esp32-gpio-pwm) 

- 2 [ESP32 脉冲宽度调制 (PWM) 信号是否可以分配任意一个 I/O 上？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/ledc.html#esp32-pwm-i-o) 

- 3 [ESP8266 NonOS SDK PWM 的变化缓慢，有哪些原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/ledc.html#esp8266-nonos-sdk-pwm) 

- 4 [ESP32 LEDC 递减渐变，Duty 值溢出错误，如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/ledc.html#esp32-ledc-duty) 

- 5 [ESP8266 通过直接写硬件定时器 FRC1 的寄存器产⽣ PWM，发现初始化 Wi-Fi 时，Wi-Fi 产⽣的中断会⼲扰硬件定时器的中断，导致错误的 PWM 输出，是否可以使⽤ FRC2 产⽣ PWM？是否可以使 FRC1 的优先级⾼于 Wi-Fi？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/ledc.html#esp8266-frc1-pwm-wi-fi-wi-fi-pwm-frc2-pwm-frc1-wi-fi) 

- 6 [使用 v3.3.3 版本 ESP-IDF 在 ESP32 设备上测试 ledc 例程，当启用了 auto light sleep，LED PWM 无输出；但不启用 auto light sleep，LED PWM 有输出。ESP-IDF 编程指南里关于 <a class="reference external" href="https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/ledc.html?highlight=pwm#id1">LED PWM</a>  的说明表示 LED PWM 在 Sleep 模式下是能工作的，请问是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/ledc.html#v3-3-3-esp-idf-esp32-ledc-auto-light-sleep-led-pwm-auto-light-sleep-led-pwm-esp-idf-led-pwm-led-pwm-sleep) 

#### 4.5.8  [电机控制脉宽调制器 (MCPWM)](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/mcpwm.html) 

#### 4.5.9  [脉冲计数器 (PCNT)](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/pcnt.html) 

#### 4.5.10  [红外遥控接收器 (RMT)](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/rmt.html) 

#### 4.5.11  [安全数字输入输出 (SDIO)](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/sdio.html) 

- 1 [ESP8266 的 SDIO 是否⽀持 SD 卡？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/sdio.html#esp8266-sdio-sd) 

- 2 [ESP32 SD 卡支持的最大容量是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/sdio.html#esp32-sd) 

- 3 [ESP32 SD 卡是否可以与 flash &amp; PSRAM 共同使用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/sdio.html#esp32-sd-flash-psram) 

- 4 [使用 ESP-WROOM-S2 模组，是否支持 SDIO 作从机？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/sdio.html#esp-wroom-s2-sdio) 

- 5 [ESP32-S2 取消了 SDIO 接口，是否还支持外接 TF 卡？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/sdio.html#esp32-s2-sdio-tf) 

- 6 [ESP32-S2 支持 eMMC 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/sdio.html#esp32-s2-emmc) 

- 7 [ESP32-S2 是否支持 SDIO 作从机？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/sdio.html#esp32-s2-sdio) 

#### 4.5.12  [SPI 控制器](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/spi.html) 

- 1 [ESP-WROOM-S2 作为从机，STM32 作为 MCU ，可以使⽤ SPI 接⼝下载吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/spi.html#esp-wroom-s2-stm32-mcu-spi) 

- 2 [ESP32 中 SPI/HSPI/VSPI 三者有什么区别呢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/spi.html#esp32-spi-hspi-vspi) 

- 3 [ESP32 使用 SPI DMA 时最大的数据传输量是 4092 字节，是因为硬件限制吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/spi.html#esp32-spi-dma-4092) 

- 4 [ESP32-S2 的 SPI 同时访问三个 SPI 从机设备，是否需要做信号量同步才能访问？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/spi.html#esp32-s2-spi-spi) 

- 5 [使用 ESP32 开发板基于 ESP-IDF release/v4.3 版本的 SDK 进行开发测试，软件编译报错如下，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/spi.html#esp32-esp-idf-release-v4-3-sdk) 

- 6 [SPI 从机支持最大速度是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/spi.html#id1) 

- 7 [使用 ESP32 作为 SPI 主机设备，在非 DMA 模式下最大可一次性传输多少字节的数据？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/spi.html#esp32-spi-dma) 

- 8 [使用 ESP32-S3-WROOM-1 (ESP32-S3R2) 模组基于 ESP-IDF v4.4 版本的 hello-world 例程开启 PSRAM 的设置后，打印如下报错，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/spi.html#esp32-s3-wroom-1-esp32-s3r2-esp-idf-v4-4-hello-world-psram) 

- 9 [使用 ESP32-S3-WROOM-2 (ESP32-S3R8V) 模组基于 ESP-IDF v4.4 版本的 hello-world 例程开启 PSRAM 的设置后，打印如下报错，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/spi.html#esp32-s3-wroom-2-esp32-s3r8v-esp-idf-v4-4-hello-world-psram) 

- 10 [使用 ESP32-C3 通过 SPI 接口驱动 LCD 液晶显示屏，是否可使用 RTC_CLK 作为 SPI 时钟，让 LCD 液晶显示屏能在 Deep-sleep 模式下正常显示静态图片？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/spi.html#esp32-c3-spi-lcd-rtc-clk-spi-lcd-deep-sleep) 

- 11 [ESP8266 RTOS SDK 是否支持 SPI 全双工？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/spi.html#esp8266-rtos-sdk-spi) 

- 12 [ESP32 能支持三线 SPI 的 9 位时钟模式（即用第 1 位表示后 8 位是命令还是数据的模式）吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/spi.html#esp32-spi-9-1-8) 

#### 4.5.13  [定时器](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/timer.html) 

- 1 [定时器如何设置中断优先级呢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/timer.html#id2) 

#### 4.5.14  [触摸传感器](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/touch.html) 

- 1 [ESP32-S2 Touch Sensor 的防水功能是在有水时屏蔽 Touch 还是有水时仍然能识别 Touch 事件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/touch.html#esp32-s2-touch-sensor-touch-touch) 

- 2 [ESP32-S2 Touch Sensor 的防水流功能在屏蔽有水流的 Touchpad 时，是否能够保持未沾水的 Pad 仍能使用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/touch.html#esp32-s2-touch-sensor-touchpad-pad) 

- 3 [是否有推荐的可以用于 Touch Sensor 测试、稳定触发 Touch Sensor 并且参数与人手触摸时参数接近的材料？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/touch.html#touch-sensor-touch-sensor) 

- 4 [Touch Sensor 的管脚能否重映射？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/touch.html#touch-sensor) 

- 5 [在覆盖亚克力板后，Touch Sensor 检测阈值是否需要重新设置？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/touch.html#id3) 

- 6 [Touch Sensor 能否检测是否有亚克力板覆盖，以便在添加或移除亚克力板时，自动切换预设定的检测阈值？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/touch.html#id4) 

- 7 [ESP32 触摸屏有哪些参考驱动？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/touch.html#id5) 

#### 4.5.15  [双线汽车接口 (TWAI)](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/twai.html) 

- 1 [ESP32 当 TWAI® 控制器处于总线关闭恢复过程中时，必须等待总线上出现 128 次总线空闲信号（连续 11 个隐性位），才能再次进⼊主动错误状态，如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/twai.html#esp32-twai-128-11) 

- 2 [ESP32 总线关闭恢复完成后，TWAI® 控制器下⼀次发送的数据可能出错（即不符合 TWAI 数据帧格式），如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/twai.html#esp32-twai-twai) 

- 3 [ESP32 TWAI® 接收到错误的数据帧可能导致下⼀次接收到的数据字节⽆效，如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/twai.html#esp32-twai) 

#### 4.5.16  [UART 控制器](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/uart.html) 

- 1 [使用 ESP8266 RTOS v3.0 以及之后的 SDK，如何将日志配置到 UART1 ？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/uart.html#esp8266-rtos-v3-0-sdk-uart1) 

- 2 [ESP32 IDF 中如何使能 UART 流控？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/uart.html#esp32-idf-uart) 

- 3 [ESP32 使用 UART0 作为通信串口，有哪些需要注意的地方？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/uart.html#esp32-uart0) 

- 4 [ESP32-SOLO-1 的 GPIO34 ～ GPIO39 是否可作为 UART 的 RX 及 TWAI® 的 RX 信号管脚？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/uart.html#esp32-solo-1-gpio34-gpio39-uart-rx-twai-rx) 

- 5 [使用 ESP32 如何动态修改串口波特率并立即生效？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/uart.html#esp32) 

- 6 [请问 ESP32 芯片支持 USRAT（Universal Synchronous Asynchronous Receiver Transmitter） 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/uart.html#esp32-usrat-universal-synchronous-asynchronous-receiver-transmitter) 

- 7 [ESP32 芯片的串口校验支持 ＭARK 和 SPACE 校验吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/uart.html#esp32-mark-space) 

- 8 [ESP8266 串口的硬件 FIFO 是多大？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/uart.html#esp8266-fifo) 

- 9 [ESP8266 的串⼝波特率范围是多大？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/uart.html#id1) 

- 10 [如何修改 UART0 的输出口?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/uart.html#uart0) 

- 11 [使用 ESP8266，想把 UART0 专门用作下载，再使用 UART1 与其他芯片通信。GPIO4 和 GPIO5 能配置成 UART1 串口吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/uart.html#esp8266-uart0-uart1-gpio4-gpio5-uart1) 

#### 4.5.17  [USB](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html) 

- 1 [ESP-IDF SDK USB 接口支持 HID、MSC 这些模式吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#esp-idf-sdk-usb-hidmsc) 

- 2 [ESP32-S2 USB 接口电流稳定输出为多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#esp32-s2-usb) 

- 3 [ESP32-S3 的 USB 支持 USB 主机吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#esp32-s3-usb-usb) 

- 4 [ESP32-C3 USB 支持 USB 串口功能和 USB JTAG 功能吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#esp32-c3-usb-usb-usb-jtag) 

- 5 [ESP32-S2 和 ESP32-S3 USB 的特征是？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#esp32-s2-esp32-s3-usb) 

- 6 [ESP32-S2 USB 主机的库和例程是否有参考？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#id1) 

- 7 [ESP32-S2 支持的 USB 协议是 OTG 1.1，速度最高是 12 Mbps。能和 USB 2.0 设备通信吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#esp32-s2-usb-otg-1-1-12-mbps-usb-2-0) 

- 8 [ESP32-S2 支持 USB 摄像头吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#id3) 

- 9 [是否有 ESP32-S2 做 U 盘 (MSC DEVICE) 的参考示例？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#esp32-s2-u-msc-device) 

- 10 [ESP32-C3 有 USB，是否不需要 cp2102 芯片就可以直接通过 USB 下载固件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#esp32-c3-usb-cp2102-usb) 

- 11 [ESP32-C3 是否支持 USB 主机？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#esp32-c3-usb) 

- 12 [ESP32-C3 芯片可以使用 USB 下载固件，但在 ESP-IDF v4.3 下不支持。如何使用 USB 下载固件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#esp32-c3-usb-esp-idf-v4-3-usb) 

- 13 [ESP32-S2 是否支持 USB HID？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#esp32-s2-usb-hid) 

- 14 [测试 <a class="reference external" href="https://github.com/espressif/esp-iot-solution/tree/usb/add_usb_solutions/examples/usb/host/usb_camera_wifi_transfer">USB 摄像头 Wi-Fi 传输</a> 例程，日志打印如下报错，是什么原因?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/usb.html#id4) 

#### 4.5.18  [其他外设](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/other-peripherals.html) 

- 1 [ESP32 是否⽀持 PCI-E 协议？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/other-peripherals.html#esp32-pci-e) 

- 2 [使用 ILI9488 LCD 屏幕测试 <a class="reference external" href="https://github.com/espressif/esp-iot-solution/tree/master/examples/screen">屏幕</a> 例程，是否支持 9-bit 总线和 18-bit 色深？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/peripherals/other-peripherals.html#ili9488-lcd-9-bit-18-bit) 

### 4.5 [协议](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/index.html) 

#### 4.6.1  [ESP-TLS](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/esp-tls.html) 

- 1 [ESP HTTPS 在使用时能跳过服务器证书校验吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/esp-tls.html#esp-https) 

- 2 [如何将 ESP-TLS 中的 <code class="docutils literal notranslate"><span class="pre">esp_tls_conn_read</span></code> API 设置成非阻塞模式？或者有其他方式来实现非阻塞？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/esp-tls.html#esp-tls-esp-tls-conn-read-api) 

- 3 [ESP-IDF 支持的 TLS 版本有哪些？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/esp-tls.html#esp-idf-tls) 

#### 4.6.2  [HTTP](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/http.html) 

- 1 [如何使用 <code class="docutils literal notranslate"><span class="pre">esp_http_client</span></code> 发送块 (chunked) 数据？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/http.html#esp-http-client-chunked) 

- 2 [ESP32 作为 HTTP 客户端，可以设置 cookie 的方式吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/http.html#esp32-http-cookie) 

- 3 [ESP32 作为 HTTP 服务器时，如何设置可同时连接的客户端个数上限？如果客户端连接个数超出上限，会出现怎样的情况？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/http.html#esp32-http) 

- 4 [ESP32 是否有至少在 HTTP/2 上实现 gRPC 客户端的示例？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/http.html#esp32-http-2-grpc) 

- 5 [在 ESP-IDF 中，如何通过 HTTP 下载文件里的某一特定段（即在头部添加 <code class="docutils literal notranslate"><span class="pre">Range:bytes</span></code> 信息）？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/http.html#esp-idf-http-range-bytes) 

#### 4.6.3  [lwIP](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html) 

- 1 [ESP8266 RTOS SDK v3.2 SNTP 校准后误差会逐渐变大，如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp8266-rtos-sdk-v3-2-sntp) 

- 2 [ESP8266 是否支持设备端自发自收？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp8266) 

- 3 [TCP/IP 默认配置的数据包长度是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#tcp-ip) 

- 4 [SNTP 协议中使用 UTC 与 GMT 的方法为何获取不到目标时区的时间？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#sntp-utc-gmt) 

- 5 [ESP32 是否有特殊的固件或者 SDK，可以不使用芯片内部的 TCP/IP 协议仅提供 AP/STA (TCP/IP bypass)，以给开发者更多的权限？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp32-sdk-tcp-ip-ap-sta-tcp-ip-bypass) 

- 6 [ESP32 &amp; ESP8266 做 TCP server 时端口释放后如何立即被再次使用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp32-esp8266-tcp-server) 

- 7 [使用 ESP32 模组下载 tcp_client 例程，通过 Wi-Fi 连接路由器，在电脑端进行 Ping 测试，偶尔出现高延时，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp32-tcp-client-wi-fi-ping) 

- 8 [使用 ESP-IDF release/v3.3 版本的 SDK ，请问以太网有设置静态 IP 的例程吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp-idf-release-v3-3-sdk-ip) 

- 9 [ESP32 有没有 LTE 连接示例？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp32-lte) 

- 10 [ESP32 TCP 反复关闭并重建 socket 时会出现内存泄漏的情况 (ESP-IDF v3.3)，原因是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp32-tcp-socket-esp-idf-v3-3) 

- 11 [ESP32 额外开启 TCP server 后对 TCP client 的最大连接数是否有限制？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp32-tcp-server-tcp-client) 

- 12 [使用 ESP32，lwIP 的 MTU 默认是多大？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp32-lwip-mtu) 

- 13 [ESP32 如何增大 DNS 请求时间？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp32-dns) 

- 14 [连续多次创建并关闭 TCP SOCKET 后出现报错 “Unable to create TCP socket: errno 23”，怎么解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#tcp-socket-unable-to-create-tcp-socket-errno-23) 

- 15 [ESP8266 收到 “tcp out of order” 的报文会怎么处理？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp8266-tcp-out-of-order) 

- 16 [ES32 支持 PPP 功能吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#es32-ppp) 

- 17 [ESP32 使用套接字中的 <code class="docutils literal notranslate"><span class="pre">read</span></code> 和 <code class="docutils literal notranslate"><span class="pre">recv</span></code> API 读取 4 KB 数据时，发现并不是每次都能读到 4 KB 的数据。这种情况如何解释？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp32-read-recv-api-4-kb-4-kb) 

- 18 [ESP-IDF 里目前使用的 lwIP 版本是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp-idf-lwip) 

- 19 [在 DHCP 模式下，ESP32 申请到 IP 后，如果租期到期，会续约此 IP 还是重新申请 IP？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#dhcp-esp32-ip-ip-ip) 

- 20 [ESP-IDF 里使用 <code class="docutils literal notranslate"><span class="pre">setsockopt</span></code> 的 <code class="docutils literal notranslate"><span class="pre">SO_SNDBUF</span></code> 选项获取或者设置发送缓冲区大小会报错，为什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp-idf-setsockopt-so-sndbuf) 

- 21 [使用 ESP-IDF 测试发现 TCP &amp; UDP 的网络数据延时较大，请问 TCP &amp; UDP 协议的缓冲数据机制是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp-idf-tcp-udp-tcp-udp) 

- 22 [ESP32 做双网卡（比如 ETH+STA）时，默认路由如何选择？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp32-eth-sta) 

- 23 [ESP-IDF 里 TCP 如何开启 keepalive？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp-idf-tcp-keepalive) 

- 24 [ESP-IDF 里可以在多线程里操作同一个套接字吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp-idf) 

- 25 [ESP DHCP 服务器模式下，ESP 设备分配到其他设备 IP 的时间是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp-dhcp-esp-ip) 

- 26 [ESP-IDF DHCP 里三个租约相关时间是指什么？具体对应代码里的什么参数？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp-idf-dhcp) 

- 27 [ESP-IDF lwIP 里每次发送数据的最大长度是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#id2) 

- 28 [使用 ESP-IDF 出现 lwIP 层相关问题需要更多的调试日志时，如何使能对应的调试日志打印（如 lwIP 下的 DHCP 和 IP 等）？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp-idf-lwip-lwip-dhcp-ip) 

- 29 [ESP-IDF 中套接字阻塞和非阻塞的区别是什么?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#id3) 

- 30 [ESP32 是否支持在连上路由后使用上一次成功连接路由器时的 IP 进行通信，如果失败再重新开始认证流程，通过 DHCP 来获取新的 IP？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/lwip.html#esp32-ip-dhcp-ip) 

#### 4.6.4  [Mbed TLS](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mbedtls.html) 

- 1 [ESP32 使用 Mbed TLS 时如何优化内存？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mbedtls.html#esp32-mbed-tls) 

#### 4.6.5  [MQTT](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mqtt.html) 

- 1 [使用 ESP8266 release/v3.3 版本的 SDK 测试 examples/protocols/esp-mqtt/tcp 例程，配置 Wi-Fi 账号、密码，连接默认配置的服务器，出现连接失败，log 如下，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mqtt.html#esp8266-release-v3-3-sdk-examples-protocols-esp-mqtt-tcp-wi-fi-log) 

- 2 [ESP-IDF 中 MQTT 组件 keepalive 的默认值是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mqtt.html#esp-idf-mqtt-keepalive) 

- 3 [MQTT 支持自动重连吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mqtt.html#id3) 

- 4 [ESP-IDF 支持的 MQTT 版本有哪些？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mqtt.html#esp-idf-mqtt) 

- 5 [ESP-IDF 里 Wi-Fi 连接断开的时候，之前 MQTT 上层协议申请的内存会自动释放吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mqtt.html#esp-idf-wi-fi-mqtt) 

- 6 [ESP32-C3 MQTT 是否能不设置对应的 <code class="docutils literal notranslate"><span class="pre">client_id</span></code> 而将 <code class="docutils literal notranslate"><span class="pre">client_id</span></code> 默认配置为空字符串？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mqtt.html#esp32-c3-mqtt-client-id-client-id) 

- 7 [使用 ESP-IDF MQTT 客户端发布 QoS 为 1 或者 2 的数据后，当 <code class="docutils literal notranslate"><span class="pre">MQTT_EVENT_PUBLISHED</span></code> 触发时是否意味着已经收到了对端合适的 ack 来证明这次发布已完成？还是仅仅只能说明成功发送了一次数据给服务器？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mqtt.html#esp-idf-mqtt-qos-1-2-mqtt-event-published-ack) 

- 8 [ESP MQTT 客户端断开连接后，如何手动释放 MQTT 资源？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mqtt.html#esp-mqtt-mqtt) 

- 9 [ESP32 Wi-Fi 和低功耗蓝牙共存时，MQTT keepalive 时间该如何配置？有没有什么合适的配置时间？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mqtt.html#esp32-wi-fi-mqtt-keepalive) 

- 10 [ESP MQTT 客户端的 disconnect 事件消息什么时候才会触发？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mqtt.html#esp-mqtt-disconnect) 

- 11 [ESP32 MQTT 客户端与服务器断开后会自动尝试重新连接吗?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mqtt.html#esp32-mqtt) 

- 12 [如何检测 ESP32 是否已经与 MQTT 服务器断开?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/mqtt.html#id4) 

#### 4.6.6  [其他协议](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/other-protocols.html) 

- 1 [ESP8285 是否⽀持 CCS (Cisco Compatible eXtensions)？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/other-protocols.html#esp8285-ccs-cisco-compatible-extensions) 

- 2 [ESP32 是否支持 LoRa (Long Range Radio) 通信？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/other-protocols.html#esp32-lora-long-range-radio) 

- 3 [ESP32-S2 在调用 <code class="docutils literal notranslate"><span class="pre">esp_netif_t*</span> <span class="pre">wifiAP </span> <span class="pre">=</span> <span class="pre">esp_netif_create_default_wifi_ap()</span></code> 后通过 <code class="docutils literal notranslate"><span class="pre">esp_netif_destroy(wifiAP)</span></code> 注销会产生 12 字节的内存泄露，什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/other-protocols.html#esp32-s2-esp-netif-t-wifiap-esp-netif-create-default-wifi-ap-esp-netif-destroy-wifiap-12) 

- 4 [如何实现证书自动下载功能 ?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/other-protocols.html#id2) 

- 5 [ESP-IDF 里如何根据错误码来获取更多的调试信息？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/other-protocols.html#esp-idf) 

- 6 [ESP8266_RTOS_SDK 是否支持 TR-069 协议？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/other-protocols.html#esp8266-rtos-sdk-tr-069) 

- 7 [ESP32 支持 SAVI 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/protocols/other-protocols.html#esp32-savi) 

### 4.6 [配置](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/provisioning.html) 

### 4.7 [安全](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html) 

- 1 [ESP8285 是否可以固件加密？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#esp8285) 

- 2 [secure boot v1 和 secure boot v2 的区别？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#secure-boot-v1-secure-boot-v2) 

- 3 [开启 secure boot 后，编译报错缺少文件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#secure-boot) 

- 4 [模组使能 secure boot 后是否可以再次烧录？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#id4) 

- 5 [模组使能 flash encrypted，重新烧录后出现 <code class="docutils literal notranslate"><span class="pre">flash</span> <span class="pre">read</span> <span class="pre">error</span></code> 错误。如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#flash-encrypted-flash-read-error) 

- 6 [ESP32 打开 flash 加密和 secure boot 后，如何关闭？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#esp32-flash-secure-boot) 

- 7 [ESP32 保护固件安全的方式有那些？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#esp32) 

- 8 [ESP32 启动 flash 加密后进行 GDB 调试，为何会不断复位重启？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#esp32-flash-gdb) 

- 9 [ESP32 芯片如何开启 Flash 加密？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#esp32-flash) 

- 10 [ESP32 的 GPIO0 拉低后无法进入下载模式，日志打印 “download mode is disable” 是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#esp32-gpio0-download-mode-is-disable) 

- 11 [在 Arduino 开发环境中使用 ESP32 能开启 secure boot 功能吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#arduino-esp32-secure-boot) 

- 12 [secure boot 和 flash 加密的使用场景？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#secure-boot-flash) 

- 13 [secure boot 和 flash 加密中涉及的存储在 eFuse 数据有哪些？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#secure-boot-flash-efuse) 

- 14 [启用 secure boot 失败，提示 “Checksum failure”，怎么解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/security.html#secure-boot-checksum-failure) 

### 4.8 [储存](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/index.html) 

#### 4.9.1  [FAT 文件系统](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/fatfs.html) 

- 1 [如何制作并烧录一个 FatFs 文件系统的镜像？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/fatfs.html#id1) 

#### 4.9.2  [非易失性存储 (NVS)](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/nvs.html) 

- 1 [NVS 是否具有磨损均衡？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/nvs.html#id2) 

- 2 [NVS 扇区是否会因写入时意外断电而损坏？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/nvs.html#id3) 

- 3 [ESP32 是否可以在外挂的 SPI flash 中挂载文件系统分区？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/nvs.html#esp32-spi-flash) 

- 4 [配置好的 Wi-Fi SSID 和 PASSWORD 在 ESP 系列开发板上重新上电后是否会消失，需要重新输入吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/nvs.html#wi-fi-ssid-password-esp) 

#### 4.9.3  [PSRAM](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/psram.html) 

- 1 [ESP32 外接 PSRAM 后，如何更改 PSRAM 的 clock 来源？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/psram.html#esp32-psram-psram-clock) 

- 2 [ESP32 模组挂载 8 MB PSRAM, 为何实际映射的只有 4 MB？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/psram.html#esp32-8-mb-psram-4-mb) 

- 3 [使用 ESP32 开发板，上面用了官方 PSRAM 芯片 PSRAM64H，当更换了另一个型号的 PSRAM 芯片后，运行 ESP-IDF 的例程并开启 PSRAM 配置，却无法正常识别，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/psram.html#esp32-psram-psram64h-psram-esp-idf-psram) 

#### 4.9.4  [SD/SDIO/MMC 驱动](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/sd-sdio-mmc.html) 

#### 4.9.5  [SPI Flash](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/spi-flash.html) 

- 1 [ESP8266 的模组，有哪些扇区可以自主使用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/spi-flash.html#esp8266) 

- 2 [ESP8266 如何读取 flash 数据？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/spi-flash.html#esp8266-flash) 

- 3 [不同的 ESP32 模组为何出现 flash 擦除时间不一致？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/spi-flash.html#id1) 

#### 4.9.6  [SPIFFS 文件系统](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/spiffs.html) 

- 1 [SPIFFS 支持磁盘加密吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/spiffs.html#id1) 

- 2 [如何将 ESP32 设备的 key 和 certs 存储到 spiffs 中呢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/spiffs.html#esp32-key-certs-spiffs) 

#### 4.9.7  [其他存储相关](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/other-storages.html) 

- 1 [ESP32 如何查看芯片内存（例如：DRAM、IRAM、rodata）使用情况？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/other-storages.html#esp32-dramiramrodata) 

- 2 [ESP8266 用户可用的 RTC RAM 是多大？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/other-storages.html#esp8266-rtc-ram) 

- 3 [如何使能 exFAT？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/other-storages.html#exfat) 

- 4 [ESP32 分区表中的分区数量有限制吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/other-storages.html#esp32) 

- 5 [ESP32 如何读取芯片剩余内存？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/other-storages.html#id3) 

- 6 [在 ESP-IDF 下使用 xTaskCreateStatic() 需要注意什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/storage/other-storages.html#esp-idf-xtaskcreatestatic) 

### 4.9 [系统](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html) 

- 1 [RTOS SDK 和 Non-OS SDK 有何区别？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#rtos-sdk-non-os-sdk) 

- 2 [ESP8266 启动时 LOG 输出 ets_main.c 有哪些原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-log-ets-main-c) 

- 3 [ESP8266 编译 Non-OS SDK 时 IRAM_ATTR 错误是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-non-os-sdk-iram-attr) 

- 4 [ESP8266 main 函数在哪里？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-main) 

- 5 [ESP8266 partition-tables 特殊注意点？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-partition-tables) 

- 6 [应用层与底层的 bin 文件可以分开编译码？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#bin) 

- 7 [ESP32 模组 flash 使用 80 Mhz 有什么注意事项吗 ？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-flash-80-mhz) 

- 8 [ESP32 系统软件复位 API？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-api) 

- 9 [使用 esp-idf 按汇编操作寄存器，是否涉及到调用不可编辑的库文件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp-idf) 

- 10 [使用 ESP-IDF 测试程序，如何设置可在单核模组上下载程序？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#id4) 

- 11 [使用 esp-idf，如何使能 ESP32 的双核模式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp-idf-esp32) 

- 12 [使用 ESP32-D0WD 芯片是否可以存储用户程序？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-d0wd) 

- 13 [ESP32 进入低功耗模式时， PSRAM 中的数据会丢失吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-psram) 

- 14 [请问 ESP32 CPU 系统时间是否由系统滴答时钟生成？精度如何？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-cpu) 

- 15 [ESP32 的 flash 和 psram 的时钟频率如何修改？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-flash-psram) 

- 16 [使用 ESP32-SOLO-1 模组，esp-idf 如何设置可在单核模组上运行？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-solo-1-esp-idf) 

- 17 [esp-idf 是否可以配置 time_t 为 64 bit ？ （现在是 32 bit）](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp-idf-time-t-64-bit-32-bit) 

- 18 [固件如何区分主芯片是 ESP8285 还是 ESP8266？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8285-esp8266) 

- 19 [ESP32 能否以动态库的方式加载库文件运行？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32) 

- 20 [ESP32 如何减小系统对 IRAM 内存的占用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-iram) 

- 21 [ESP32 light sleep 例程为何会自动唤醒？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-light-sleep) 

- 22 [ESP32 deep_sleep例程测试，为何当 const int wakeup_time_sec = 3600时，程序 crash 出现死循环？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-deep-sleep-const-int-wakeup-time-sec-3600-crash) 

- 23 [ESP32 有几种系统复位方式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#id6) 

- 24 [ESP8266-NONOS-V3.0 版本的 SDK，报错如下，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-nonos-v3-0-sdk) 

- 25 [ESP32 是否可以完整使用 8MB PSRAM 内存？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-8mb-psram) 

- 26 [ESP8266 AT 连接 AP 后，系统默认进入 modem-sleep，但电流未明显下降有哪些原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-at-ap-modem-sleep) 

- 27 [ESP32 是否可以永久更改 MAC 地址？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-mac) 

- 28 [ESP8266 进行 ota 升级时如何校验 all.bin 为非法文件？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-ota-all-bin) 

- 29 [IDF 版本更新后，更新说明在哪里？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#idf) 

- 30 [ESP8266 是否有详细的寄存器⼿册？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266) 

- 31 [ESP32 开启 Secure Boot 后 无法正常启动 ,出现如下报错，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-secure-boot) 

- 32 [ESP8266 如何在设备软重启的情况下保留数据？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#id7) 

- 33 [ESP8266 有哪些定时器可用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#id8) 

- 34 [ESP8266 的看⻔狗是什么作⽤？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#id9) 

- 35 [ESP8266 user_init 内有那些注意事项？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-user-init) 

- 36 [ESP32 同时开启 “Enable debug tracing of PM using GPIOs” 和 “Allow .bss segment placed in external memory” 后为何会导致系统不停重启？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-enable-debug-tracing-of-pm-using-gpios-allow-bss-segment-placed-in-external-memory) 

- 37 [ESP32 IDF v3.3 版本 bootloader 运行 v3.1 版本 APP bin , 程序为何会触发 RTCWDT_RTC_RESET ？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-idf-v3-3-bootloader-v3-1-app-bin-rtcwdt-rtc-reset) 

- 38 [ESP32 芯片出厂是否有唯一的 chip_id ？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-chip-id) 

- 39 [ESP8266 rst curse 如何查看？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-rst-curse) 

- 40 [ESP32 编译生成的 bin 文件大小如何优化？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-bin) 

- 41 [ESP32 是否有系统重新启动的 API ？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#id11) 

- 42 [ESP32 异常 log <cite>invalid header: 0xffffffff</cite>](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-log-invalid-header-0xffffffff) 

- 43 [ESP8266 deep sleep 定时唤醒机制是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-deep-sleep) 

- 44 [ESP32 使用 heap_caps_get_free_size 获取 RAM 约 300 KB，为何与手册 520K 存在差异？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-heap-caps-get-free-size-ram-300-kb-520k) 

- 45 [ESP32 &amp; ESP8266 如何通过局域网的 APP 进行 OTA 升级？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-esp8266-app-ota) 

- 46 [ESP32 如何修改 LOG 输出至串口 UART1 ?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-log-uart1) 

- 47 [ESP8266 使用 MQTT ssl_mutual_auth 通讯，在 OTA 时出现如下报错：](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-mqtt-ssl-mutual-auth-ota) 

- 48 [ESP32 配置 menuconfig –&gt; Component config 中有 NVS 选项，为何配置项目为空？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-menuconfig-component-config-nvs) 

- 49 [ESP32 上电或 Deep-sleep 醒来后，会随机发⽣⼀次看⻔狗复位?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-deep-sleep) 

- 50 [ESP32 CPU 使⽤ cache 访问外部 SRAM 时，如果这些操作需要 CPU 同时处理，可能会发⽣读写错误?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-cpu-cache-sram-cpu) 

- 51 [ESP32 CPU 访问外设时，如果连续不间断地通过 DPORT 写同⼀个地址，为何会出现数据丢失的现象？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-cpu-dport) 

- 52 [ESP32 CPU 频率从 240 MHz 直接切换到 80/160 MHz 会卡死，如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-cpu-240-mhz-80-160-mhz) 

- 53 [ESP32 同时有 GPIO 和 RTC_GPIO 功能的 pad 的上拉下拉电阻只能由 RTC_GPIO 的上拉下拉寄存器控制，如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-gpio-rtc-gpio-pad-rtc-gpio) 

- 54 [ESP32 由于 flash 启动的速度慢于芯⽚读取 flash 的速度，芯⽚上电或 Deep-sleep 醒来后，会随机发⽣⼀次看⻔狗复位，如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-flash-flash-deep-sleep) 

- 55 [ESP32 CPU 在访问外部 SRAM 时会⼩概率发⽣读写错误, 如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-cpu-sram) 

- 56 [ESP32 双核情况下，⼀个 CPU 的总线在读 A 地址空间，⽽另⼀个 CPU 的总线在读 B 地址空间，读 B 地址空间的 CPU可能会发⽣错误如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-cpu-a-cpu-b-b-cpu) 

- 57 [ESP32 CPU 通过读取 INTERRUPT_REG 寄存器来复位 CAN 控制器的中断信号。如果在同⼀个 APB 时钟周期内 CAN 控制器刚好产⽣发送中断信号，则发送中断信号丢失，如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-cpu-interrupt-reg-can-apb-can) 

- 58 [ESP32 ECO V3 芯⽚，当程序同时满⾜下列条件时，会出现 live lock（活锁）现象，导致 CPU ⼀直处于访存状态，不能继续执⾏指令，请问如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-eco-v3-live-lock-cpu) 

- 59 [ESP32 CPU 访问 <code class="docutils literal notranslate"><span class="pre">0x3FF0_0000</span> <span class="pre">~</span> <span class="pre">0x3FF1_EFFF</span></code> 与 <code class="docutils literal notranslate"><span class="pre">0x3FF4_0000</span> <span class="pre">~</span> <span class="pre">0x3FF7_FFFF</span></code> 两段地址空间存在限制，如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-cpu-0x3ff0-0000-0x3ff1-efff-0x3ff4-0000-0x3ff7-ffff) 

- 60 [ESP32 如何关闭程序 LOG 输出？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-log) 

- 61 [ESP8266 在 Deep sleep 模式下，保存在 RTC Memory 里的数据是否可运行？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-deep-sleep-rtc-memory) 

- 62 [ESP32 的 NVS 的 Key 的最大长度为多大？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-nvs-key) 

- 63 [ESP-IDF release/v4.2 里的 cJSON 支持 uint64_t 的数据解析吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp-idf-release-v4-2-cjson-uint64-t) 

- 64 [未启用 Flash 加密的 ESP32 可以进行 GDB 调试，但启动 Flash 加密后进行 GDB 调试时，设备一直重启，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#flash-esp32-gdb-flash-gdb) 

- 65 [ESP32 使用手机热点进行 OTA 固件下载时，关闭流量开关几秒后再次打开会出现程序一直卡死在 OTA 里的情况（使用路由器时插拔 wan 口网线同理），是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-ota-ota-wan) 

- 66 [ESP32-C3 在 Deep-Sleep 模式下可以通过哪些 GPIO 进行唤醒？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-c3-deep-sleep-gpio) 

- 67 [使用 ESP-WROOM-02D 模组，电池供电，在低电量（模组勉强启动）的时候，频繁格式化读写 flash 有什么风险吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp-wroom-02d-flash) 

- 68 [ESP32 如何查看线程使用过的最大栈大小？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#id13) 

- 69 [使用 ESP32 时打印 “SW_CPU_RESET” 日志是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-sw-cpu-reset) 

- 70 [使用 ESP32 时，单独测试 NVS 发现占用内存很大，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-nvs) 

- 71 [如何修改模块的系统时间 ?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#id14) 

- 72 [OTA 升级过程中 esp_ota_end 返回 ESP_ERR_OTA_VALIDATE_FAILED 报错，如何排查这类问题?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#ota-esp-ota-end-esp-err-ota-validate-failed) 

- 73 [ESP8266-RTOS-SDK 如何将数据存储在 RTC memory 中？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-rtos-sdk-rtc-memory) 

- 74 [在 Deep-sleep 模式唤醒后，ESP8266 是从哪里启动的？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#deep-sleep-esp8266) 

- 75 [RTC 时钟什么时候会被重置？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#rtc) 

- 76 [ESP32 使用 AT+GSLP 指令进入 Deep-sleep 模式后，是否可通过拉低 EN 进行唤醒？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-at-gslp-deep-sleep-en) 

- 77 [当多个线程要使用 ESP32 的看门狗时，是否每个线程都要开启看门狗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#id16) 

- 78 [使用 ESP8266-RTOS-SDK release/v3.3，如何进入 Light-sleep 模式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp8266-rtos-sdk-release-v3-3-light-sleep) 

- 79 [ESP8266 在 Deep sleep 模式下如何唤醒？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#id18) 

- 80 [使用 ESP32-WROVER 模组，休眠时存在电池抖动或异常掉电上电导致死机无法唤醒的问题，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-wrover) 

- 81 [如何烧录自定义 mac 地址？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#mac) 

- 82 [ESP32 在使用 esp_timer 时，出现网络通信或者蓝牙通信异常，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-esp-timer) 

- 83 [使用 ESP32，请问 ULP 里面用 <code class="docutils literal notranslate"><span class="pre">jump</span></code> 跳转到一个函数，是否有返回的指令？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/system.html#esp32-ulp-jump) 

### 4.10 [Wi-Fi](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html) 

- 1 [ESP32 和 ESP8266 是否支持中文 SSID？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-esp8266-ssid) 

- 2 [[Scan] ESP32 扫描⼀次需要花多长时间？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#scan-esp32) 

- 3 [[Scan] 乐鑫是否支持 boundary scans(边界扫描)？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#scan-boundary-scans) 

- 4 [客户⾃研产品如何优化⼆次谐波等杂散？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id1) 

- 5 [Wi-Fi 信道是什么？可以自行选择信道吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id2) 

- 6 [80 MHz 倍频杂散较差该如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#mhz) 

- 7 [[LWIP] 使用 ESP-IDF v4.1，ESP32 用作 SoftAP 模式时如何设置 IP 地址?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#lwip-esp-idf-v4-1-esp32-softap-ip) 

- 8 [[LWIP] ESP32 Station 模式，如何设置静态 IP？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#lwip-esp32-station-ip) 

- 9 [[LWIP] ESP-IDF 里如何设置 DHCP Server 的 Option 内容？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#lwip-esp-idf-dhcp-server-option) 

- 10 [[Performance] 如何测试 Wi-Fi 模组的通信速率？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#performance-wi-fi) 

- 11 [[LWIP] ESP8266 SoftAP 默认使用哪个网段？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#lwip-esp8266-softap) 

- 12 [[Connect] ESP8266 SoftAP 模式支持几个设备？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-esp8266-softap) 

- 13 [ESP8266/ESP32/ESP32-S2 是否支持 web/softAP 配网？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp8266-esp32-esp32-s2-web-softap) 

- 14 [[Connect] ESP8266 和 ESP32 作为 softap 模式如何隐藏 SSID？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-esp8266-esp32-softap-ssid) 

- 15 [esp_wifi_802.11_tx 接口中的 buffer 参数中包括 FCS 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp-wifi-802-11-tx-buffer-fcs) 

- 16 [ESP-WROOM-32D 支持的 Wi-Fi 频段信息和功率表分别是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp-wroom-32d-wi-fi) 

- 17 [ESP32 Wi-Fi RF 功率最高值是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-wi-fi-rf) 

- 18 [ESP32 如何调整 Wi-Fi 的发射功率？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-wi-fi) 

- 19 [[Connect] ESP32 AP 模式最多支持多少设备连接？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-esp32-ap) 

- 20 [[Connect] Wi-Fi 模组如何通过 RSSI 数值划分信号强度等级？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-wi-fi-rssi) 

- 21 [[Connect] ESP32 做 soft-AP 时为什么会把 STA 踢掉？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-esp32-soft-ap-sta) 

- 22 [[Connect] ESP32 进行 Wi-Fi 连接时，如何通过错误码判断失败原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-esp32-wi-fi) 

- 23 [ESP32 系列芯片每次连接服务器都会执行域名解析吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32) 

- 24 [[Connect] Wi-Fi Log 中状态机切换后面数字的含义？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-wi-fi-log) 

- 25 [[Connect] bcn_timeout, ap_probe_send_start 是什么意思？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-bcn-timeout-ap-probe-send-start) 

- 26 [[Connect] Wi-Fi 连接断开后如何重连？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-wi-fi) 

- 27 [[Connect] ESP32 作为 station 时什么时候会把 SoftAP 踢掉？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-esp32-station-softap) 

- 28 [[Scan] 为什么有时候扫描不到 AP？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#scan-ap) 

- 29 [[Scan] 最多能够扫描多少个 AP？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id6) 

- 30 [[Scan] 连接时周围存在多个相同 ssid/password 时能否选出最佳 AP 连接？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#scan-ssid-password-ap) 

- 31 [[Scan] wifi_sta_config_t 中 scan_method 怎么配置？全信道扫描和快速扫描的区别在哪里？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#scan-wifi-sta-config-t-scan-method) 

- 32 [[LWIP] 如何获取 socket 的错误码？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#lwip-socket) 

- 33 [[LWIP] 默认 TCP keep-alive 时间为多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#lwip-tcp-keep-alive) 

- 34 [[LWIP] TCP 重传间隔？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#lwip-tcp) 

- 35 [[LWIP] 最多能够创建多少个 socket ？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id7) 

- 36 [[Sleep] ESP32 有哪几种休眠方式及其区别是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#sleep-esp32) 

- 37 [[Sleep] ESP32 modem sleep 降频功能在哪打开？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#sleep-esp32-modem-sleep) 

- 38 [[Sleep] ESP32 modem sleep 降频功能最低能降到多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id8) 

- 39 [[Sleep] ESP32 modem sleep 平均电流大小影响因素？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id9) 

- 40 [[Sleep] 为什么测到的 modem sleep 平均电流偏高？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#sleep-modem-sleep) 

- 41 [[Sleep] 为什么测到的 light sleep 平均电流偏高？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#sleep-light-sleep) 

- 42 [ESP8266 是否支持 802.11k/v/r 协议？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp8266-802-11k-v-r) 

- 43 [ESP32 Wi-Fi 支持相同的 SSID 不同的 AP 之间漫游吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-wi-fi-ssid-ap) 

- 44 [[Connect] NONOS_SDK <cite>2.1.0</cite> 升级到 <cite>2.2.2</cite> 后，连接时间变长？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-nonos-sdk-2-1-0-2-2-2) 

- 45 [ESP32 如何收发 Wi-Fi 802.11 数据包？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-wi-fi-802-11) 

- 46 [[Connect] ESP32 系列 &amp; ESP8266 路由器连接失败有哪些可能原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-esp32-esp8266) 

- 47 [[Connect] ESP8266 有那些配网方式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-esp8266) 

- 48 [[Connect] SmartConfig 配⽹ Wi-Fi 参数信息有哪些要求？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-smartconfig-wi-fi) 

- 49 [[Connect] ESP8266 Wi-Fi 是否支持 WPA2 企业级加密？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-esp8266-wi-fi-wpa2) 

- 50 [[Connect] ESP32 保持 Wi-Fi 连接的低功耗模式有哪些？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id10) 

- 51 [乐鑫芯片是否支持 WPA3？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#wpa3) 

- 52 [[Connect] 当环境内存在多个相同 SSID 时，设备如何连接 ？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-ssid) 

- 53 [[Connect] ESP8266 有中继器方案吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id11) 

- 54 [ESP-NOW 是什么？有哪些优势与场景？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp-now) 

- 55 [ESP32 数据帧和管理帧的重传次数是多少？是否可以配置？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id13) 

- 56 [ESP32 如何自定义 hostname？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-hostname) 

- 57 [如何获取 802.11 无线数据包？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id14) 

- 58 [ESP32 Wi-Fi 支持 PMF(Protected Management Frames) 和 PFS(Perfect Forward Secrecy) 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-wi-fi-pmf-protected-management-frames-pfs-perfect-forward-secrecy) 

- 59 [ESP32 IDF v4.1 Wi-Fi 怎样获取 AP 的 RSSI？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-idf-v4-1-wi-fi-ap-rssi) 

- 60 [ESP32 IDF v4.1 Wi-Fi 怎样获取已连接的 AP 的 RSSI？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id15) 

- 61 [ESP8266 在使用 esptouch v2 出现 AES PN 错误 log？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp8266-esptouch-v2-aes-pn-log) 

- 62 [ESP32 WFA 认证支持 Multicast 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-wfa-multicast) 

- 63 [使用 ESP32，是否可以在建立热点之前，先扫描所有的 AP 以及所占用的信道，从中选择一个占用最小最干净的信道来建立自己的 AP 呢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-ap-ap) 

- 64 [使用 ESP32 ，ESP-IDF 版本为 release/v3.3，Wi-Fi Scan 时，当有多个相同的 ssid 时，获取的列表中有多个重复的 SSID，是否有 API 进行过滤，只保留一个 SSID？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-esp-idf-release-v3-3-wi-fi-scan-ssid-ssid-api-ssid) 

- 65 [ESP8266 是否支持 EDCF (AC) 方案？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp8266-edcf-ac) 

- 66 [使用 master 版本的  ESP8266-RTOS-SDK，开启 Wi-Fi Qos 应用获得 EDCF 的支持，请问 ESP8266 是如何决定哪个数据包应该分配到 EDCF AC 类别的?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#master-esp8266-rtos-sdk-wi-fi-qos-edcf-esp8266-edcf-ac) 

- 67 [使用 ESP-IDF release/v4.2 版本的 SDK，如何在 AP 模式下开启 mDNS 功能？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp-idf-release-v4-2-sdk-ap-mdns) 

- 68 [ESP-NOW 是否可以同时与 Wi-Fi 一起使用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp-now-wi-fi) 

- 69 [使用 ESP32，在不考虑内存与功耗的情况下，如何配置最大 Wi-Fi 传输速度与稳定性呢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id16) 

- 70 [ESP8266 作为 Wi-Fi SoftAP 模式，最多支持多少个 Station 设备连接？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp8266-wi-fi-softap-station) 

- 71 [使用 ESP32 设备作为 Station 模式，如何获取 CSI 数据?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-station-csi) 

- 72 [ESP32 在 AP + STA 模式连接 Wi-Fi 后，任意开启关闭 AP 模式是否会影响 Wi-Fi 连接？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-ap-sta-wi-fi-ap-wi-fi) 

- 73 [ESP32 使用 release/v3.3 版本的 ESP-IDF 进行开发，只需要蓝牙功能，如何通过软件关闭 Wi-Fi 功能？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-release-v3-3-esp-idf-wi-fi) 

- 74 [使用 ESP-IDF 开发，esp_wifi_80211_tx() 接口只能发送数据包，是否有对应的接收函数接口？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp-idf-esp-wifi-80211-tx) 

- 75 [esptouch 配网失败概率较高的原因有哪些？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esptouch) 

- 76 [ESP32 使用 Wi-Fi 时 IRAM 不足，如何优化？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-wi-fi-iram) 

- 77 [ESP32 如何测试 Wi-Fi 传输距离？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id18) 

- 78 [使用 ESP32，Wi-Fi MTU 的长度最大能设置多大？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-wi-fi-mtu) 

- 79 [ESP32 模组挂机测试有时会打印类似如下 log，代表什么含义？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-log) 

- 80 [ESP32 在 AP + STA 模式下，如何关闭 AP 模式?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-ap-sta-ap) 

- 81 [ESP32 使用 Wi-Fi 的功能后，是否 ADC2 的所有通道都不能使用了？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-wi-fi-adc2) 

- 82 [Wi-Fi 模块如何设置国家码？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id19) 

- 83 [当 ESP32 用作 SoftAP 连接苹果手机时，手机提示”低安全性　WPA/WPA2(TKIP) 并不安全。如果这是您的无线局域网，请配置路由器以使用 WPA2(AES) 或 WPA3 安全类型“，该如何解决？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-softap-wpa-wpa2-tkip-wpa2-aes-wpa3) 

- 84 [ESP32 的 Wi-Fi 模块仅支持 2.4 GHz 频率的带宽，如果在进行连网配置时使用 2.4G 和 5G 多频合一的路由器，Wi-Fi 能否配网成功？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-wi-fi-2-4-ghz-2-4g-5g-wi-fi) 

- 85 [ESP32 用作 AP 模式时如何获取连接进来的 station 的 RSSI？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-ap-station-rssi) 

- 86 [ESP32 支持 FTM(Fine Timing Measurement) 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-ftm-fine-timing-measurement) 

- 87 [当 ESP32 设置为 STA+AP 共存时，能否指定通过 STA 或者 AP 接口发送数据？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-sta-ap-sta-ap) 

- 88 [ESP8266 wpa2_enterprise  如何开启 Wi-Fi 调试功能?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp8266-wpa2-enterprise-wi-fi) 

- 89 [Wi-Fi 信号格数有对应标准吗?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id21) 

- 90 [WFA 漏洞修复最新情况？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#wfa) 

- 91 [Wi-Fi 连接失败时产生的错误码代表什么?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id23) 

- 92 [使用 ESP32 Release/v3.3 版本的 SDK 下载 Station 例程，无法连接不加密的 Wi-Fi ，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-release-v3-3-sdk-station-wi-fi) 

- 93 [ESP32-S2 芯片，Wi-Fi 通信的最大速度是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-s2-wi-fi) 

- 94 [log 信息中打印如下 <code class="docutils literal notranslate"><span class="pre">I</span> <span class="pre">(81447377)</span> <span class="pre">wifi:new:&lt;7,0&gt;,</span> <span class="pre">old:&lt;7,2&gt;,</span> <span class="pre">ap:&lt;255,255&gt;,</span> <span class="pre">sta:&lt;7,0&gt;,</span> <span class="pre">prof:1</span></code> 代表什么意思?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#log-i-81447377-wifi-new-7-0-old-7-2-ap-255-255-sta-7-0-prof-1) 

- 95 [ESP 模块是否支持 EAP-FAST?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp-eap-fast) 

- 96 [ESP 模块支持 WiFi NAN (Neighbor Awareness Networking) 协议吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp-wifi-nan-neighbor-awareness-networking) 

- 97 [使用 ESP32，ESP-IDF 版本为 release/v3.3， 配置路由器时，是否有 API 可以直接判断输入的密码不正确？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-esp-idf-release-v3-3-api) 

- 98 [基于 ESP-IDF v4.4 版本的 SDK 测试 ESP32 的 Station 例程，如何支持 WPA3 加密模式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp-idf-v4-4-sdk-esp32-station-wpa3) 

- 99 [ESP32 如何加快 Wi-Fi 的连接速度？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#id25) 

- 100 [ESP32 WPA2 企业级认证是否支持 Cisco CCKM 模式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-wpa2-cisco-cckm) 

- 101 [使用 wpa2_enterprise（EAP-TLS 方式），客户端证书最大支持长度是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#wpa2-enterprise-eap-tls) 

- 102 [ESP8089 是否支持 Wi-Fi Direct 模式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp8089-wi-fi-direct) 

- 103 [环境中有很多 AP，ESP32 如何连接 RSSI 不低于配置阈值的 AP?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#ap-esp32-rssi-ap) 

- 104 [ESP32 Wi-Fi 出现信标丢失 (beacon lost) 且在 6 秒钟之后给 AP 发 5 个探测请求 (probe request)，此时 AP 没回应就会导致断开连接，这个 6 秒钟可以配置吗?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-wi-fi-beacon-lost-6-ap-5-probe-request-ap-6) 

- 105 [ESP32 Wi-Fi 可以使用 PSRAM 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#esp32-wi-fi-psram) 


-------------------------------------------------------
## 5 [硬件相关](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/index.html) 

### 5.1 [芯片功能对比](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/chip-comparison.html) 

- 1 [ESP32 ECO V3 芯⽚在软硬件使⽤上和之前版本的芯片有什么区别呢？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/chip-comparison.html#esp32-eco-v3) 

- 2 [ESP32 的 GPIO34 ~ GPIO39 管脚是否只能设置为输入模式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/chip-comparison.html#esp32-gpio34-gpio39) 

- 3 [ESP32 有适配 Linux 平台驱动吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/chip-comparison.html#esp32-linux) 

- 4 [模组屏蔽盖上的二维码扫描数据如何解读？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/chip-comparison.html#id5) 

- 5 [ESP32 的 VDD3P3_RTC 是否支持单独电池供电？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/chip-comparison.html#esp32-vdd3p3-rtc) 

- 6 [ESP32-PICO-D4 和 ESP32-PICO-V3 以及 ESP32-PICO-V3-02 有什么区别？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/chip-comparison.html#esp32-pico-d4-esp32-pico-v3-esp32-pico-v3-02) 

- 7 [ESP 模块支持 Thread 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/chip-comparison.html#esp-thread) 

- 8 [ESP 模组支持 WAPI (Wireless LAN Authentication and Privacy Infrastructure) 功能吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/chip-comparison.html#esp-wapi-wireless-lan-authentication-and-privacy-infrastructure) 

- 9 [ESP8266 是否支持 32 MHz 晶振频率？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/chip-comparison.html#esp8266-32-mhz) 

- 10 [ESP32 是否支持 Zephyr？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/chip-comparison.html#esp32-zephyr) 

### 5.2 [开发板使用](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html) 

- 1 [ESP-EYE 开发板运行发热过高如何改善？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp-eye) 

- 2 [开发板不使用 USB 供电，如何使用管脚供电？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#usb) 

- 3 [ESP8266 连接手机热点，出现如下报错，有哪些原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp8266) 

- 4 [开发板 ESP32-Korvo-DU1906 中 DU1906 芯片音频数据通过什么协议与 ESP32 交互？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32-korvo-du1906-du1906-esp32) 

- 5 [是否有支持 POE 供电的以太网开发板？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#poe) 

- 6 [ESP32S2-Kaluga 中为什么 Audio 和 Camera 不能共用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32s2-kaluga-audio-camera) 

- 7 [ESP32S2-Kaluga 是否支持蓝牙语音？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32s2-kaluga) 

- 8 [ESP32S2-Kaluga 上的 Codec 芯片是否自带功放？最大支持外接多大功率的喇叭？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32s2-kaluga-codec) 

- 9 [ESP32-S2-Kaluga-1 是否有并行 LCD 接口？如果有，硬件上需要如何使用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32-s2-kaluga-1-lcd) 

- 10 [ESP32S2-Kaluga 是否支持 USB 调试？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32s2-kaluga-usb) 

- 11 [ESP32S2-Kaluga 中为什么需要多加一块数字 mic 芯片，不可以直接使用 ADC 采集吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32s2-kaluga-mic-adc) 

- 12 [ESP32S2-Kaluga 中的 speaker 与 Audio_Out 接口是否支持同时输出？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32s2-kaluga-speaker-audio-out) 

- 13 [ESP32S2-Kaluga-V1.2 中的 I2C <em>FPC</em> CNN 接口如何使用？是否有相关的 Demo？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32s2-kaluga-v1-2-i2c-fpc-cnn-demo) 

- 14 [ESP32S2-Kaluga-V1.2 中的 4.3inch <em>LCD</em> FPC_CNN 接口是否为并口 LCD 接口？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32s2-kaluga-v1-2-4-3inch-lcd-fpc-cnn-lcd) 

- 15 [ESP32S2-Kaluga-V1.2 PCB上有很多没有焊接元件的地方是否是运送过程中丢失？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32s2-kaluga-v1-2-pcb) 

- 16 [ESP32-S2-Kaluga-V1.2 开发板配有摄像头，是否有摄像头的例程可以提供？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32-s2-kaluga-v1-2) 

- 17 [是否可以单独购买 ESP32S2-Kaluga 的子板？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#id2) 

- 18 [ESP32 DevKitc 开发板 LED 灯不亮，设备管理器也无法找到该设备？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32-devkitc-led) 

- 19 [文档中有提到 EN 按键，但在购买的开发板上没有找到该按键？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#en) 

- 20 [使用 ESP32 开发板，连接 Windwos 电脑后未在设备管理器中找到串口，有哪些原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32-windwos) 

- 21 [使用 ESP32-LyraT-V4.3 音频开发板，长按 Boot 按键也很难进入下载模式，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32-lyrat-v4-3-boot) 

- 22 [使用 ESP-WROOM-02D 模组，复位信号持续多久后模组会进入复位状态？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp-wroom-02d) 

- 23 [ESP32-LyraT-Mini 开发板的原理图中将 ES8311 codec 芯片的模拟量输出连接到了 ES7243 ADC 芯片的输入，这样做的目的是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32-lyrat-mini-es8311-codec-es7243-adc) 

- 24 [使用 ESP32-mini-1 模组，串口上电打印 log 如下，是什么原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/development-board.html#esp32-mini-1-log) 

### 5.3 [硬件设计](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html) 

- 1 [ESP32 在 Light-sleep 模式下如何避免 VDD3P3_RTC 管脚的电压掉电？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-light-sleep-vdd3p3-rtc) 

- 2 [ESP32 管脚配置需要注意什么事项？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#id2) 

- 3 [乐鑫芯片 GPIO 最大承载电压？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#gpio) 

- 4 [ESP8266 电压电流需求？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp8266) 

- 5 [乐鑫 Wi-Fi 模组是否有单面板 PCB 的方案？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#wi-fi-pcb) 

- 6 [ESP8266 电池供电有哪些要求？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#id3) 

- 7 [如何获取 ESP32 系列芯片 footprint？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-footprint) 

- 8 [使用 ESP32-S2 芯片，用了 DVP camera 接口后还能接入语音吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-s2-dvp-camera) 

- 9 [使用 ESP32 模块，使用 GPIO0、GPIO4 作为 I2C 信号接口，需要注意什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-gpio0gpio4-i2c) 

- 10 [ESP32 的外接 flash 占用了 GPIO6 ~ GPIO11，这 6 个 IO 是否还能作为 SPI 来使用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-flash-gpio6-gpio11-6-io-spi) 

- 11 [使用 ESP8285 芯片时，是否需要连接外部晶振？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp8285) 

- 12 [ESP32-D2WD 外接 PSRAM 的参考设计？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-d2wd-psram) 

- 13 [ESP32 是否可以用 PWM 或 DAC 来播放音乐？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-pwm-dac) 

- 14 [为什么 ESP32 模组和 ESP32 芯片的建议工作电压范围不一样？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-esp32) 

- 15 [自主设计模组 flash 擦除速度相比乐鑫模组较慢有哪些原因？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#flash) 

- 16 [ESP8266 为何上电瞬间会电流较大？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#id6) 

- 17 [ESP32 以太网 RMII 时钟选择有哪些？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-rmii) 

- 18 [ESP32-LyraT 开发板扬声器接口规格？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-lyrat) 

- 19 [基于 ESP32 设计的模组，哪些管脚无法被用户使用？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#id7) 

- 20 [ESP32 如何使用管脚复位芯片？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#id8) 

- 21 [ESP8266 供电设计需要注意哪些问题？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#id10) 

- 22 [ESP8266 使用 TOUT 管脚做 ADC 采样时，超过 0 V ~ 1.0 V 是否会损坏管脚？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp8266-tout-adc-0-v-1-0-v) 

- 23 [使用板载天线的模组，对 PCB 和外壳设计有哪些要求？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#pcb) 

- 24 [使用 ESP32 GPIO34 ~ GPIO39 是否可作为 UART 的 RX ？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-gpio34-gpio39-uart-rx) 

- 25 [ESP32 模组外接 32 kHz 晶振参考设计？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-32-khz) 

- 26 [ESP32 模组 flash 是否支持 80 MHz 的 QIO 模式？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-flash-80-mhz-qio) 

- 27 [如何配置 ESP32 以太网的 RMII 同步时钟？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#id13) 

- 28 [使用 ESP8266 芯片如何进行硬件复位？硬件复位信号是低电平有效还是高电平有效？复位的条件是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#id14) 

- 29 [乐鑫原理图中的 <code class="docutils literal notranslate"><span class="pre">NC</span></code> 缩写是什么意思？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#nc) 

- 30 [如何在 ESP32-S2 中使用多天线？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-s2) 

- 31 [ESP32-C3F SPI CS0 是否需要外接 10 kΩ 上拉电阻？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-c3f-spi-cs0-10-k) 

- 32 [ESP-Skainet 有语音识别硬件设计参考吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp-skainet) 

- 33 [硬件上是否有必要接 32 kHz 的 RTC 晶振？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#khz-rtc) 

- 34 [使用 ESP32-MINI-1 模组，是否可提供 Altium Designer 的元件库？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-mini-1-altium-designer) 

- 35 [ESP8266 的 UART0 的输入电压能由 3.3 V 改为 1.8 V 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp8266-uart0-3-3-v-1-8-v) 

- 36 [ESP8266 UART0 的电平是由 VDD 决定的，还是由 VDDPST 决定的？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp8266-uart0-vdd-vddpst) 

- 37 [ESP32-D2WD 芯片外接 PSRAM 软件配置注意事项是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#id16) 

- 38 [ESP32 芯片当 VDD 供电从 0 V 慢慢升到 3.3 V 时，芯片为何无法正常启动？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-vdd-0-v-3-3-v) 

- 39 [使用 ESP32-WROOM-32D 模组，是否可以使用 GPIO12 用作其他功能？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-wroom-32d-gpio12) 

- 40 [ESP32-WROOM-32D 模组的外接 flash，是否可以不使用 GPIO6 ~ GPIO11 的接口？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-wroom-32d-flash-gpio6-gpio11) 

- 41 [ESP32 芯片设计模组，PCB 板是否需要加屏蔽盖？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-pcb) 

- 42 [ESP32 的 I2S 的 CLK 管脚必须使用 GPIO0、GPIO1 或 GPIO3 吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/hardware-design.html#esp32-i2s-clk-gpio0gpio1-gpio3) 

### 5.4 [射频相关](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/RF-related.html) 

- 1 [乐鑫芯片支持的调制方式有哪些？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/RF-related.html#id3) 

- 2 [如何获取乐鑫产品的 RF 相关的信息（如天线描述、天线辐射图等）用于认证？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/RF-related.html#rf) 

- 3 [ESP32 使用 RF Test Tool 时为什么在高温 80 °C 下运行会自动降低发射功率？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/RF-related.html#esp32-rf-test-tool-80-c) 

- 4 [ESP32-WROVER-E 模组如何提高 Wi-Fi 信号的接收距离和强度？(应用场景：Wi-Fi 探针)](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/RF-related.html#esp32-wrover-e-wi-fi-wi-fi) 

- 5 [如何烧写 phy_init 数据到 flash 中？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/RF-related.html#phy-init-flash) 

### 5.5 [工艺与防护](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/process-and-ESD.html) 

### 5.6 [生产测试](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/production-test.html) 

- 1 [如何获取产测工具?](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/production-test.html#id2) 

- 2 [ESP32 使用 <code class="docutils literal notranslate"><span class="pre">esptool.py</span> <span class="pre">burn_custom_mac</span></code> 命令写入用户自定义 MAC 地址，为什么通过 <code class="docutils literal notranslate"><span class="pre">esptool.py</span> <span class="pre">read_mac</span></code> 读到的还是出厂默认的 MAC 地址？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/hardware-related/production-test.html#esp32-esptool-py-burn-custom-mac-mac-esptool-py-read-mac-mac) 


-------------------------------------------------------
## 6 [测试校验](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/test-verification/index.html) 

### 6.1 [功耗测试指南](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/test-verification/power-consumption-verification.html) 

- 1 [休眠⽅式有哪⼏种？有什么区别？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/test-verification/power-consumption-verification.html#id2) 

- 2 [ESP32 Deep-sleep 可以通过任意 RTC_GPIO 唤醒吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/test-verification/power-consumption-verification.html#esp32-deep-sleep-rtc-gpio) 

- 3 [ESP8266 的 CHIP_PU 管脚为低电平时，芯片的功耗是多少？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/test-verification/power-consumption-verification.html#esp8266-chip-pu) 


-------------------------------------------------------
## 7 [商务问题](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/index.html) 

### 7.1 [你们的产品通过哪些认证？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#id2) 

### 7.2 [请问贵司是否获得 ISO 质量管理体系认证？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#iso) 

### 7.3 [请问你们芯片和模组通过了 REACH、ROHS 等环保认证吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#reachrohs) 

### 7.4 [你们在国内、欧洲、美国或加拿大有代理商吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#id3) 

### 7.5 [请问如何能成为乐鑫的代理商？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#id4) 

### 7.6 [贵司的产品信息在哪里可以查看？ 量产产品有哪些？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#id5) 

### 7.7 [你们的产品有⻓期供货保证吗？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#id6) 

### 7.8 [如何查看产品的标准包装量 (SPQ) 和最小起订量 (MOQ)？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#spq-moq) 

### 7.9 [如何购买你们的产品？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#id7) 

### 7.10 [请问批量采购价格是多少？如何批量采购？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#id8) 

### 7.11 [请问你们各产品之间，有什么区别？包括不同系列与型号等。](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#id9) 

### 7.12 [贵司模组本身有固件吗？我需要定制模组/芯片烧录，请问可否在出厂时候完成？价格如何？交期多久？我应如何操作？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#id10) 

### 7.13 [请问哪款产品支持 HomeKit？如何获取 Espressif HomeKit SDK？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#homekit-espressif-homekit-sdk) 

### 7.14 [请问贵司的办公地点在哪里？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#id11) 

### 7.15 [请问你们技术的联系方式是什么？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#id12) 

### 7.16 [请问如何与贵司取得联系？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#id13) 

### 7.17 [请问如何可以快速识别贵司的模组为量产产品或 NPI 新品？](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/commercial-faq/#npi) 
