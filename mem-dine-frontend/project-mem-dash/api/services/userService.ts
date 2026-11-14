
import { API_BASE_URL, USER_ENDPOINTS } from '../apiEndpoints'

// Request structure
export interface UserCredentials {
    username: string
    password: string
}

// Backend response structure
export interface ApiResponse<T = unknown> {
    status: 'success' | 'error'
    status_code: number
    data: T
}

export interface ApiErrorResponse {
    error: string
}

// User service
export const userService = {

    // Create a new user
    async createUser(
        credentials: UserCredentials
    ): Promise<ApiResponse> {

        const response = await fetch(
            `${API_BASE_URL}${USER_ENDPOINTS.CREATE_USER}`,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(credentials)
            }
        )

        return await response.json()
    },

    // Check user credentials
    async checkUser(
        credentials: UserCredentials
    ): Promise<ApiResponse> {

        const response = await fetch(
            `${API_BASE_URL}${USER_ENDPOINTS.CHECK_USER}`,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(credentials)
            }
        )

        return await response.json()
    }
}
