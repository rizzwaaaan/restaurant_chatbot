import axios from 'axios';

const API_URL = "http://localhost:5000";

export const fetchMenu = async (type, category) => {
    const response = await axios.get(`${API_URL}/menu?type=${type}&category=${category}`);
    return response.data;
};
