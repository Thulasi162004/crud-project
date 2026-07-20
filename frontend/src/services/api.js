import axios from "axios";

const API = axios.create({
  baseURL: "https://crud-project-backend-gceg.onrender.com",
});

export default API;