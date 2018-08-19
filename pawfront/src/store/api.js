import axios from 'axios'
import qs from 'qs'

// axios 配置
// axios.defaults.timeout = 5000
// axios.defaults.baseURL = 'http://118.24.42.37:6800/'
axios.defaults.baseURL = 'http://127.0.0.1:6800/'

// pawclient实例
let pawclient = axios.create({
  baseURL: 'http://127.0.0.1:8000'
  //   baseURL: 'http://118.24.42.37:8000'
})

// 默认响应拦截器，拦截异常
axios.interceptors.response.use((res) => {
  return res
}, (err) => {
  if (err && err.response) {
    console.log(err)
    console.log(err.response.status)
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
// pawclient响应拦截器，拦截异常
pawclient.interceptors.response.use((res) => {
  return res
}, (err) => {
  if (err && err.response) {
    console.log(err)
    console.log(err.response.status)
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

function apiAxios(method, url, params, contentType) {
  if (params !== null && params.ispaw === true) {
    return new Promise((resolve, reject) => {
      pawclient({
        method: method,
        url: url,
        data: method !== 'GET' || method === 'PUT' ? (contentType === 'application/x-www-form-urlencoded' ? qs.stringify(params) : params) : null,
        params: method === 'GET' || method === 'DELETE' ? params : null,
        headers: {'Content-Type': contentType}
      })
        .then(response => {
          if (response.data) {
            resolve(response.data)
          } else {
            resolve(response.data)
          }
        })
        .catch()
    })
  } else {
    return new Promise((resolve, reject) => {
      axios({
        method: method,
        url: url,
        data: method !== 'GET' || method === 'PUT' ? (contentType === 'application/x-www-form-urlencoded' ? qs.stringify(params) : params) : null,
        params: method === 'GET' || method === 'DELETE' ? params : null,
        headers: {'Content-Type': contentType}
      })
        .then(response => {
          if (response.data) {
            resolve(response.data)
          } else {
            resolve(response.data)
          }
        })
        .catch((error) => {
          console.log(error)
          reject(error)
        })
    })
  }
}

/**
 * 获取所有项目
 */
export function listprojects() {
  return apiAxios('get', '/listprojects.json', null, 'text/plain')
}

/**
 * 获取所有项目
 */
export function listjobs(project) {
  return apiAxios('get', '/listjobs.json?project=' + project, null, 'application/json')
}

/**
 * 获取日志
 */
export function listlog(param) {
  return apiAxios('post', '/manager/log/', param, 'application/json')
}

/**
 * 获取定义好的所有项目
 */
export function listdefinedprojects(param) {
  return apiAxios('get', '/manager/project/', param, 'application/json')
}

/**
 * 保存项目
 */
export function saveproject(param) {
  return apiAxios('post', '/manager/project/', param, 'application/json')
}

/**
 * 更新项目
 */
export function updateproject(param) {
  return apiAxios('put', '/manager/project/' + param.id + '/', param, 'application/json')
}

/**
 * 获得项目
 */
export function getproject(param) {
  return apiAxios('get', '/manager/project/' + param.id + '/', param, 'application/json')
}

/**
 * 删除项目
 */
export function delproject(param) {
  return apiAxios('delete', '/manager/project/' + param.id + '/', param, 'application/json')
}

/**
 * 部署项目
 */
export function deployproject(param) {
  return apiAxios('put', '/manager/deploy/', param, 'application/json')
}

/**
 * 取消部署项目
 */
export function canceldployproject(param) {
  return apiAxios('post', '/delproject.json', param, 'application/x-www-form-urlencoded')
}

/**
 * 通过project名字查找所有版本信息
 */
export function listversionsbyprojectname(param) {
  return apiAxios('get', '/listversions.json?project=' + param.name, param, 'application/json')
}

/**
 * 通过project名字查找所有爬虫信息
 */
export function listspidersbyprojectname(param) {
  return apiAxios('get', '/listspiders.json?project=' + param.name, param, 'application/json')
}

/**
 * 部署爬虫
 */
export function schedule(param) {
  return apiAxios('post', '/schedule.json', param, 'application/x-www-form-urlencoded')
}

/**
 * 删除部署中或者运行中的爬虫
 */
export function cancel(param) {
  return apiAxios('post', '/cancel.json', param, 'application/x-www-form-urlencoded')
}
