import React from "react";
import ReservationForm from "../components/ReservationForm";
import "../styles/Reservation.css";

function Reservation() {
  return (
    <div className="reservation">
      <h2>Book a Table</h2>
      <ReservationForm />
    </div>
  );
}

export default Reservation;
