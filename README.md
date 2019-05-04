# spider

- 分析:

  - 确定URL

    - http://fy.iciba.com/ajax.php?a=fy

  - 请求方法: POST

  - 确定数据

    ```
    f: auto
    t: auto
    w: 你好
    ```

  - 确定请求头



* 实现思路:
  * 获取要翻译的内容
  * 准备翻译URL
  * 准备翻译的数据
  * 发请求, 获取响应内容
  * 解析响应内容, 打印翻译结果
