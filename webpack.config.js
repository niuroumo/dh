const path = require('path')
const webpack = require('webpack')

module.exports = {
    watch:true,
    mode:'development',
    entry:{
        index:'./src/index.js',
        search:'./src/search.js'
    },
    output:{
        filename:'bundle.js',
        path:path.resolve(__dirname,'src')
    },
    module:{
        rules:[
            { 
                test: /\.js$/,
                use: 'babel-loader' 
            },
            { 
                test: /\.css$/,
                use: ['style-loader','css-loader']
            },
            { 
                test: /\.less$/,
                use: ['style-loader','css-loader','less-loader']
            },
            { 
                test: /\.(woff|woff2|eot|ttf|otf)$/,
                use: 'file-loader'
            },
            { 
                test: /\.(png|jpg|gif)$/,
                use: 'file-loader'
            },
        ]
    },
    plugins:[
        new webpack.HotModuleReplacementPlugin()
    ],
    devServer:{
        host:'127.0.0.1',
        port:'8080',
        hot:true,
        contentBase:'./src'
    }
}