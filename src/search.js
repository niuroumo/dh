import React from 'react'
import ReactDOM from 'react-dom'
import './css/search.less'
import logo from './images/logo.png'

class Search extends React.Component{
    render(){
        return <div class="search-text">
            搜索模块fjdakd <img src={ logo } />
        </div>
    }
}

ReactDOM.render(
    <Search />,
    document.getElementById('root')
)