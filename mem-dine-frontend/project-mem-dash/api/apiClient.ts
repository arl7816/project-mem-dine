import { API_BASE_URL } from "./apiEndpoints"

// Backend response structure
export interface ApiResponse<T = unknown> {
    status: 'success' | 'error'
    status_code: number
    data: T
}

export interface ApiErrorResponse {
    error: string
}


export const apiClient = {
    
    async callEndpoint(
        endPoint: string,
        credentials: any,
        methodType: string = "POST"
    ): Promise<ApiResponse>{
        const response = await fetch(
            `${API_BASE_URL}${endPoint}`,
            {
                method: methodType,
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(credentials)
            }
        )

        return await response.json()
    }

}
