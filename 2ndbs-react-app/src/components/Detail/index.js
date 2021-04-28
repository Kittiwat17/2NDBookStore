import React, { Component } from "react";

export default class Detail extends Component {
    render() {
        return (
            <div>
                <div class="grid-container2">
                    <div class="custom-card2">
                        <div class="row">
                            <div class="col">
                                <img class="pic" src={"https://m.media-amazon.com/images/I/514axA2lwpL.jpg"} width="450px" heigh="450px" />
                            </div>
                            <div class="col">
                                <h1>Learning React Native</h1>
                                <p>ผู้แต่ง :</p>
                                <p>ปีที่พิมพ์ : </p> <p>ภาษา : </p>
                                <p>วันที่ประกาศ :</p>
                                <p>ผู้ลงขาย :</p>
                                <p>ช่องทางการติดต่อ :</p>
                                <p>รายละเอียด : *************************</p>
                                <p>ราคา :</p>
                                <h5>Comment</h5>
                                <div class="comment-area"> <textarea class="form-control" placeholder="" rows="4"></textarea> </div>
                                <div class="comment-btns mt-2">
                                    <div class="row">
                                        <div class="col-6">
                                        </div>
                                        <div class="col-6">
                                            <div class="pull-right"> <button class="btn btn-success send btn-sm">Send <i class="fa fa-long-arrow-right ml-1"></i></button> </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}