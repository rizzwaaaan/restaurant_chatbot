import React, { useEffect, useState } from "react";
import MenuCard from "../components/MenuCard";
import { fetchMenu } from "../api/api";
import "../styles/Menu.css";

function Menu() {
  const [menuItems, setMenuItems] = useState([]);

  useEffect(() => {
    fetchMenu().then(data => setMenuItems(data));
  }, []);

  return (
    <div className="menu">
      <h2>Our Menu</h2>
      <div className="menu-grid">
        {menuItems.map((item) => (
          <MenuCard key={item.id} item={item} />
        ))}
      </div>
    </div>
  );
}

export default Menu;
