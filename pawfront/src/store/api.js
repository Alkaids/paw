import axios from 'axios'

// axios 配置
// axios.defaults.timeout = 5000
// 跨域是否使用凭证，默认关闭，若不开启，登陆后无法正常获取api资源
// axios.defaults.withCredentials = true
// axios.defaults.baseURL = 'http://192.168.50.117:8081/'
axios.defaults.baseURL = 'http://localhost:6800/'
// pawclient实例
let pawclient = axios.create({
  baseURL: 'http://127.0.0.1:8000'
})

// 响应拦截器，拦截异常
axios.interceptors.response.use((res) => {
  return res
}, (err) => {
  if (err && err.response) {
    switch (err.response.status) {
      case 400:
        err.message = '请求错误(400)'
        break
      case 401:
        err.message = '未授权，请重新登录(401)'
        break
      case 403:
        err.message = '拒绝访问(403)'
        break
      case 404:
        err.message = '请求出错(404)'
        break
      case 408:
        err.message = '请求超时(408)'
        break
      case 500:
        err.message = '服务器错误(500)'
        break
      case 501:
        err.message = '服务未实现(501)'
        break
      case 502:
        err.message = '网络错误(502)'
        break
      case 503:
        err.message = '服务不可用(503)'
        break
      case 504:
        err.message = '网络超时(504)'
        break
      case 505:
        err.message = 'HTTP版本不受支持(505)'
        break
      default:
        err.message = `连接出错(${err.response.status})!`
    }
  } else {
    err.message = '连接服务器失败!'
  }
  return Promise.reject(err)
})

function PostFetch(url, params, contentType) {
  if (params.ispaw === true) {
    return new Promise((resolve, reject) => {
      pawclient.post(url, params, {
        headers: {
          'Content-Type': contentType
        }
      }, {
        validateStatus: status => {
          return status !== 200
        }
      })
        .then(response => {
          if (response.data) {
            resolve(response.data)
          } else {
            resolve(response.data)
          }
        })
        .catch((error) => {
          if (error.response) {
            console.log(error.response.data)
          } else if (error.request) {
            console.log(error.request)
          } else {
            console.log('Error', error.message)
          }
          console.log(error.config)
          reject(error)
        })
    })
  } else {
    return new Promise((resolve, reject) => {
      axios.post(url, params, {
        headers: {
          'Content-Type': contentType
        }
      }, {
        validateStatus: status => {
          return status !== 200
        }
      })
        .then(response => {
          if (response.data) {
            resolve(response.data)
          } else {
            resolve(response.data)
          }
        })
        .catch((error) => {
          if (error.response) {
            console.log(error.response.data)
          } else if (error.request) {
            console.log(error.request)
          } else {
            console.log('Error', error.message)
          }
          console.log(error.config)
          reject(error)
        })
    })
  }
}

function GetFetch(url, contentType) {
  return new Promise((resolve, reject) => {
    axios.get(url, {
      headers: {
        'Content-Type': contentType
      }
    }, {
      validateStatus: status => {
        return status !== 200
      }
    })
      .then(response => {
        if (response.data) {
          resolve(response.data)
        } else {
          resolve(response.data)
        }
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response.data)
        } else if (error.request) {
          console.log(error.request)
        } else {
          console.log('Error', error.message)
        }
        console.log(error.config)
        reject(error)
      })
  })
}

/**
 * 获取所有项目
 */
export function listprojects() {
  return GetFetch('/listprojects.json', 'application/json')
}

/**
 * 获取所有项目
 */
export function listjobs(project) {
  return GetFetch('/listjobs.json?project=' + project, 'application/json')
}

/**
 * 获取日志
 */
export function listlog(param) {
  return PostFetch('/manager/log/', param, 'application/json')
}
