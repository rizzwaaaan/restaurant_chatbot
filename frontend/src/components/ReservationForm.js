import { useState } from "react";

const ReservationForm = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    date: "",
    time: "",
    seats: 1,
    paymentMethod: "cash",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Reservation Data:", formData);
    alert("Reservation Confirmed!");
  };

  return (
    <div className="max-w-lg mx-auto bg-gray-900 p-6 rounded-lg shadow-lg text-white">
      <h2 className="text-xl font-bold mb-4">Book a Reservation</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block mb-1">Full Name</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
            className="w-full p-2 rounded bg-gray-800 border border-gray-600"
          />
        </div>

        <div>
          <label className="block mb-1">Email</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
            className="w-full p-2 rounded bg-gray-800 border border-gray-600"
          />
        </div>

        <div>
          <label className="block mb-1">Date</label>
          <input
            type="date"
            name="date"
            value={formData.date}
            onChange={handleChange}
            required
            className="w-full p-2 rounded bg-gray-800 border border-gray-600"
          />
        </div>

        <div>
          <label className="block mb-1">Time</label>
          <input
            type="time"
            name="time"
            value={formData.time}
            onChange={handleChange}
            required
            className="w-full p-2 rounded bg-gray-800 border border-gray-600"
          />
        </div>

        <div>
          <label className="block mb-1">Number of Seats</label>
          <input
            type="number"
            name="seats"
            min="1"
            max="10"
            value={formData.seats}
            onChange={handleChange}
            required
            className="w-full p-2 rounded bg-gray-800 border border-gray-600"
          />
        </div>

        <div>
          <label className="block mb-1">Payment Method</label>
          <select
            name="paymentMethod"
            value={formData.paymentMethod}
            onChange={handleChange}
            className="w-full p-2 rounded bg-gray-800 border border-gray-600"
          >
            <option value="cash">Cash</option>
            <option value="card">Credit/Debit Card</option>
            <option value="upi">UPI</option>
          </select>
        </div>

        <button
          type="submit"
          className="w-full p-2 bg-blue-600 rounded hover:bg-blue-700"
        >
          Confirm Reservation
        </button>
      </form>
    </div>
  );
};

export default ReservationForm;
