import axios from 'axios'

//const API_URL = process.production.env.REACT_APP_API_URL;
const API_URL = process.env.REACT_APP_API_URL;
export const getAllData = axios.create({
    baseURL: API_URL,
});

export default getAllData;