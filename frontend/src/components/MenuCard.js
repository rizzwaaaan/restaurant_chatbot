import React from "react";
import "../styles/MenuCard.css";

function MenuCard({ item }) {
  return (
    <div className="menu-card">
      <img src={item.image} alt={item.name} />
      <h3>{item.name}</h3>
      <p>{item.description}</p>
      <p><strong>₹{item.price}</strong></p>
    </div>
  );
}

export default MenuCard;
