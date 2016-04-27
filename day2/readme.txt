1. hello.txt是给处理文件的代码读写操作使用的,文件1,2,3
2. 7_编写类似sed命令的文件替换脚本
   说明：开发文件替换小程序:将 hello.txt 中 Nina 替换为 521
	./file_replace.py 'Nina' '521' hello.txt
	./file_replace.py 'Nina' '521' hello.txt --bak new_hello.txt	