
import { USER_ENDPOINTS } from '../apiEndpoints'
import type { ApiResponse } from '../apiClient'
import { apiClient } from '../apiClient'
import type { Api } from '@vitejs/plugin-vue'

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
    },

    async login(
        credentials: UserCredentials
    ): Promise<ApiResponse>{
        return await apiClient.callEndpoint(
            USER_ENDPOINTS.LOGIN,
            credentials
        )
    },

    async logout(): Promise<ApiResponse>{
        return await apiClient.callEndpoint(
            USER_ENDPOINTS.LOGOUT,
            {}
        )
    },

    async me(): Promise<ApiResponse>{
        return await apiClient.getEndpoint(
            USER_ENDPOINTS.ME,
            "include"
        )
    }

}
