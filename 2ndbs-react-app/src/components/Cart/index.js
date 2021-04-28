import React, { Component } from "react";

export default class Cart extends Component {
    render() {
        return (
            <div>
                <h1 class="font-weight-bold">Your Cart</h1>
                <div class="container">
                    <div class="col" >

                        <div class="col-sm border-bottom border-top">
                            <p><img src={"https://m.media-amazon.com/images/I/514axA2lwpL.jpg"} width="450px" heigh="450px" />
                            Learning React Native 350
                    <button type="button" class="btn btn-danger">ลบ</button>
                            </p>
                    </div>
                    <div class="col-sm border-bottom">
                        <p><img src={"https://m.media-amazon.com/images/I/514axA2lwpL.jpg"} width="450px" heigh="450px" />
                    Learning React Native 350
                    <button type="button" class="btn btn-danger">ลบ</button>
                        </p>
                    </div>
                    <div class="col-sm border-bottom">
                        <p><img src={"https://m.media-amazon.com/images/I/514axA2lwpL.jpg"} width="450px" heigh="450px" />
                    Learning React Native 350
                    <button type="button" class="btn btn-danger">ลบ</button>
                        </p>
                    </div>
                </div>
            </div></div >
        );
    }
}