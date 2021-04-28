import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar/Navbar'
import Main from './components/Main'
import "./style.css";
import Profile from './components/Profile/index'
import {Route, NavLink} from 'react-router-dom'
import Detail from './components/Detail/index'
import Cart from './components/Cart/index'

function App() {
  return (
    <div>
      <Navbar/>
      {/* <Main/> */}
      {/* <Profile/> */}
      <Detail/>
      {/* <Cart/> */}
    </div>
  );
}

export default App;
