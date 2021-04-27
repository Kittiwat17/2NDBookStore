import React from "react";

export default function Navbar() {
    return (
        <nav class="navbar navbar-expand-lg navbar-light navbar-custom">
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item active">
                        <a class="nav-link" href="#">หน้าหลัก<span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">โพสต์ประกาศขาย</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">โพสต์ประกาศซื้อ</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled" href="#">2nd store Bookstore</a>
                    </li>
                </ul>
            </div>
            <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"/>
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
        </nav>

    );
}