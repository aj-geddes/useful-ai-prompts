# Network Service with URLSession

## Network Service with URLSession

```swift
class NetworkService {
  static let shared = NetworkService()

  private let session: URLSession
  private let baseURL: URL

  init(
    session: URLSession = .shared,
    baseURL: URL = URL(string: "https://api.example.com")!
  ) {
    self.session = session
    self.baseURL = baseURL
  }

  func fetch<T: Decodable>(
    _: T.Type,
    from endpoint: String
  ) async throws -> T {
    let url = baseURL.appendingPathComponent(endpoint)
    var request = URLRequest(url: url)
    request.addAuthHeader()

    let (data, response) = try await session.data(for: request)
    try validateResponse(response)

    let decoder = JSONDecoder()
    decoder.dateDecodingStrategy = .iso8601
    return try decoder.decode(T.self, from: data)
  }

  func put<T: Decodable, Body: Encodable>(
    _: T.Type,
    to endpoint: String,
    body: Body
  ) async throws -> T {
    let url = baseURL.appendingPathComponent(endpoint)
    var request = URLRequest(url: url)
    request.httpMethod = "PUT"
    request.addAuthHeader()
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    let encoder = JSONEncoder()
    encoder.dateEncodingStrategy = .iso8601
    request.httpBody = try encoder.encode(body)

    let (data, response) = try await session.data(for: request)
    try validateResponse(response)

    let decoder = JSONDecoder()
    return try decoder.decode(T.self, from: data)
  }

  private func validateResponse(_ response: URLResponse) throws {
    guard let httpResponse = response as? HTTPURLResponse else {
      throw NetworkError.invalidResponse
    }

    switch httpResponse.statusCode {
    case 200...299:
      return
    case 401:
      throw NetworkError.unauthorized
    case 500...599:
      throw NetworkError.serverError
    default:
      throw NetworkError.unknown
    }
  }
}

enum NetworkError: LocalizedError {
  case invalidResponse
  case unauthorized
  case serverError
  case unknown

  var errorDescription: String? {
    switch self {
    case .invalidResponse: return "Invalid response"
    case .unauthorized: return "Unauthorized"
    case .serverError: return "Server error"
    case .unknown: return "Unknown error"
    }
  }
}

extension URLRequest {
  mutating func addAuthHeader() {
    if let token = KeychainManager.shared.getToken() {
      setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
    }
  }
}
```
