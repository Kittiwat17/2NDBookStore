import React, { Component } from "react";

export default class Profile extends Component {
    render() {
        return (
            <div class="grid-container">
                <div class="item1"><p>Profile</p>
                <img class="img2" src="https://image.flaticon.com/icons/png/512/64/64572.png"/>
                <p><button type="button" class="btn btn-info">แก้ไขข้อมูลส่วนตัว</button></p>
                </div>
                <div class="item2">
                    <p>My Book</p>
                    <div class="custom-card">
                        <img src={"https://m.media-amazon.com/images/I/514axA2lwpL.jpg"} width="450px" heigh="450px" />
                    </div>
                    <div class="custom-card">
                        <img src={"https://m.media-amazon.com/images/I/514axA2lwpL.jpg"} width="450px" heigh="450px" />
                    </div>
                </div>
            </div>
        );
    }
}