直接运行不成功
废话不多说，上解决方案
`Step1`：`npm cache clean --force`
`Step2`：`rm -rf node_modules`
`Step3`：`rm -rf package-lock.json`
`Step4`：`npm install`
npm install 成功之后再次启动

=====================================================>

其实执行上面的命令之吼还是不会成功，
需要新创建一个项目
vue init webpack 项目名
然后将这个项目中的一些配置文件
复制到新的项目中，比如一些配置文件和静态文件，以及写好的单文件组件

<=====================================================

# meiduo_mall

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
