import axios from "axios";

axios.defaults.baseURL = "http://localhost:5000";
axios.defaults.headers.post["Access-Control-Allow-Origin"] = "*";

const api = axios.create();

export default api;