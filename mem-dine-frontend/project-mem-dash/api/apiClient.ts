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
    
    /** Calls a endpoint via the fetch method */
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
    },

    /** Converts a error response to a string to read */
    extractErrorMessageFromResponse(
        response: ApiResponse, 
        defaultMessage: string = "Something went wrong"
    ): string{
        const errorData = response?.data as ApiErrorResponse;
        return errorData.error ?? defaultMessage;
    }

}
