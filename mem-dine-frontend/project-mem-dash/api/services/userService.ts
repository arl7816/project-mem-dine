
import { USER_ENDPOINTS } from '../apiEndpoints'
import type { ApiResponse } from '../apiClient'
import { apiClient } from '../apiClient'

// Request structure
export interface UserCredentials {
    username: string
    password: string
}

// User service
export const userService = {

    // Create a new user
    async createUser(
        credentials: UserCredentials
    ): Promise<ApiResponse> {

        return await apiClient.callEndpoint(
            USER_ENDPOINTS.CREATE_USER,
            credentials
        )
    },

    // Check user credentials
    async checkUser(
        credentials: UserCredentials
    ): Promise<ApiResponse> {

        return await apiClient.callEndpoint(
            USER_ENDPOINTS.CHECK_USER,
            credentials
        )
    }
}
