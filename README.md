#RestBlog
重新发明车轮，用上有趣的技术  


##基本想法
*  博客系统，为了专注于技术，采用熟悉的业务逻辑
*  采用RESTful架构
  *  数据库采mongo,sqlite
  *  后端
    *  先使用django1.7(django-rest-framework）
      *  数据模型可以模仿现有的博客
    *  再用expres.js写一编
    *  再用文件系统写一遍,模仿pelican，使用markdown语法
  *  前端采用angular.js，为了学习edX，也试着使用backbone.js  
*  用上前端自动化技术,静态文件自动化处理，包括coffee的预编译，Sass的预编译，趁机学习（grunt(使用插件),npm(调用bash)）
*  使用git分支来管理不同的技术版本
*  模仿其他项目时，采用github的库内搜索阅读关键源码
*  新的技术新的想法，通过合理的架构不断融入进来，比如为它写vim插件啦，安卓客户端啦，用Scheme重写啦
