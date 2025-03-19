import axios from "axios";

const API_URL = "http://localhost:5050";  // ✅ Updated to match Flask port

export const fetchMenu = async (type, category) => {
  try {
    const response = await axios.get(`${API_URL}/menu`, {
      params: { type, category },  // ✅ Use Axios params
    });
    return response.data;
  } catch (error) {
    console.error("❌ Error fetching menu:", error);
    return []; // Return empty array on error
  }
};
