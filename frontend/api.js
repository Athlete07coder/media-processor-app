import axios from "axios";

export const processMedia = async (data) => {
  return await axios.post("http://localhost:8000/process", data);
};