import React, { Component } from "react";

export default class Store extends Component {
    render() {
        const { id, name, img, detail } = this.props.shop;
        console.log(this.props.shop);
        return (
                <div class="custom-card">
                    <img src={img} width="450px" heigh="450px" />
                    <div class="card-body border-top">
                        <h5>{name}</h5>
                        <p>{detail}</p>
                    </div>
                </div>
        );
    }
}