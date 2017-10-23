# cloudstore
    - which common used to upload file to qiniu cdn service
    
# install
    - 1 pip install qiniu
    - 2 pip install tornado
    
# usage
    ## server:
        启动：在conf/config.py 中设置启动端口
                1 python start startup.py & 也可以；
                2 也可以自行编写system.service 通过systemctl来启动；

    ## client 接口使用:
	   ### 请求说明:
	   	1 功能:	文件上传至七牛CDN
		2 请求方式：POST
	    3 请求url：/upload
		4 请求参数：
			|参数名称	|类型	    |是否必须	    |描述
			|type		|string	    |是		        |媒体类型，主要分为图片或者视频,image | video
			|bucket		|string	    |是		        |上传的命名空间名称,test1|test2 
			|key		|string	    |是		        |上传至cdn的uri名称（比如key如果为upload/test，上传成功后的访问url为http://xxxxx/upload/test）,首字符不能为/
			|file			    |是		        |要上传的文件

	    ### 返回说明：
		    eg:
			[
  				{
    					"message": "upload success",
    					"data": "http://www.liyang.com/upload/test.png",
    					"status": 0
  				}
			]		
		
		### 返回参数:
			|参数名称		|类型               |描述
			|status		   |int	               |返回状态码，0 成功，1 失败	
			|data		   |string	       |返回url，成功返回具体的访问url地址，失败返回空
			|message	   |string	       |上传成功或者失败的具体信息。
