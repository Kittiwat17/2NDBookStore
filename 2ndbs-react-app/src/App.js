import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar/Navbar'
import Main from './components/Main'
import "./style.css";
import Profile from './components/Profile/index'
import {Route, NavLink} from 'react-router-dom'

function App() {
  return (
    <div className="App">
      <Navbar/>
      <Main/>
      {/* <Profile/> */}
    </div>
  );
}

export default App;
