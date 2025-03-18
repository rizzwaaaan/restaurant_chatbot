import React from "react";
import { Link } from "react-router-dom";
import "../styles/Navbar.css";

function Navbar() {
  return (
    <nav className="navbar">
      <h1>Restaurant Bot</h1>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/menu">Menu</Link></li>
        <li><Link to="/reservation">Reservation</Link></li>
        <li><Link to="/order">Order</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
