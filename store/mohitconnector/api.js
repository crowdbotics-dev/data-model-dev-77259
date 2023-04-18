import axios from "axios"
import {
  MOHIT_CONNECTOR_USERNAME,
  MOHIT_CONNECTOR_PASSWORD
} from "react-native-dotenv"
const mohitconnector = axios.create({
  baseURL: "https://youtube.com",
  auth: {
    username: MOHIT_CONNECTOR_USERNAME,
    password: MOHIT_CONNECTOR_PASSWORD
  },
  headers: { Accept: "application/json", "Content-Type": "application/json" }
})
function mohitconnector_get_testing_read(payload) {
  return mohitconnector.get(`/testing`)
}
export const apiService = { mohitconnector_get_testing_read }
