import React, { Component } from "react";
import Store from '../Store';
import {shopdata} from '../../data.js'

export default class Main extends Component{
    state={
        shops:shopdata
    }
    render(){
        const {shops}=this.state;
        return(
            <div>
                <h1>หนังสือทั้งหมด</h1>
            <div class="list-card-grid">
                {shops.map(shop=>(
                    <Store key={shop.id} shop={shop}/>
                ))}
            </div>
            </div>
        )
    }
}