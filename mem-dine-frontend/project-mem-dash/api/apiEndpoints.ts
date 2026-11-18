export const API_BASE_URL = "http://localhost:5000/"

export const USER_ENDPOINTS = {
    CREATE_USER: "user/create_user",
    CHECK_USER: "user/check_user",
    LOGIN: "user/login",
    LOGOUT: "user/logout",
    ME: "user/me"
} as const
