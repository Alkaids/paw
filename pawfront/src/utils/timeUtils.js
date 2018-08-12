import moment from 'moment'

moment.locale('zh-cn')

export function timeFormat(time) {
  return moment(time).format('YYYY-MM-DD HH:mm:ss')
}

export function timeReduce(start, end) {
  return moment(end).diff(moment(start)) / 1000
}
