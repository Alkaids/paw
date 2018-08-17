<template>
  <div class="main-content">
    <vue-topprogress ref="topProgress"></vue-topprogress>
    <div class="button-tool">
      <el-popover
        placement="right"
        width="450"
        trigger="click">
        <el-form :inline="true">
          <el-form-item style="margin-bottom: 0!important;">
            <el-input v-model="interval" auto-complete="off">
              <template slot="append">秒刷新一次</template>
            </el-input>
          </el-form-item>
          <el-form-item style="margin-bottom: 0!important;">
            <el-button type="primary" size="mini"
                       @click="intervalLoadStartOrStop()">开始自动刷新
            </el-button>
          </el-form-item>
        </el-form>
        <el-button slot="reference" size="mini" type="primary" style="margin-left: 10px">{{intervaltext}}</el-button>
      </el-popover>
      <el-button type="primary" size="mini" v-show="this.intervalid!==0"
                 @click="intervalLoadStartOrStop()">停止自动刷新
      </el-button>
    </div>
    <el-collapse>
      <el-collapse-item>
        <template slot="title">
          <h4 class="left-title"> 部署中任务
          </h4>
        </template>
        <div class="pending-table">
          <el-table
            :data="pending"
            style="width: 100%">
            <el-table-column
              label="项目"
              prop="project"
              sortable
              min-width="10%"
              header-align="center"
            />
            <el-table-column
              label="爬虫"
              prop="spider"
              sortable
              min-width="10%"
              header-align="center"
            />
            <el-table-column
              label="id"
              prop="id"
              sortable
              min-width="25%"
              header-align="center"
            />
            <el-table-column
              label="开始时间"
              prop="start_time"
              sortable
              min-width="15%"
              header-align="center"
            />
            <el-table-column
              label="结束时间"
              prop="end_time"
              sortable
              min-width="15%"
              header-align="center"
            />
            <el-table-column
              label="已执行"
              prop="exec_time"
              min-width="10%"
              header-align="center"
            />
            <el-table-column label="操作" header-align="center" min-width="15%">
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  @click="handleEdit(scope.$index, scope.row)">编辑
                </el-button>
                <el-button
                  size="mini"
                  type="danger"
                  @click="handleDelete(scope.$index, scope.row)">删除
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-collapse-item>
      <el-collapse-item>
        <template slot="title">
          <h4 class="left-title"> 进行中任务
          </h4>
        </template>
        <div class="running-table">
          <el-table
            :data="running"
            style="width: 100%">
            <el-table-column
              label="项目"
              prop="project"
              sortable
              min-width="10%"
              header-align="center"
            />
            <el-table-column
              label="爬虫"
              prop="spider"
              sortable
              min-width="10%"
              header-align="center"
            />
            <el-table-column
              label="id"
              prop="id"
              sortable
              min-width="25%"
              header-align="center"
            />
            <el-table-column
              label="开始时间"
              prop="start_time"
              sortable
              min-width="15%"
              header-align="center"
            />
            <el-table-column
              label="结束时间"
              prop="end_time"
              sortable
              min-width="15%"
              header-align="center"
            />
            <el-table-column
              label="已执行"
              prop="exec_time"
              min-width="10%"
              header-align="center"
            />
            <el-table-column label="操作" header-align="center" min-width="15%">
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  @click="handleEdit(scope.$index, scope.row)">编辑
                </el-button>
                <el-button
                  size="mini"
                  type="danger"
                  @click="handleDelete(scope.$index, scope.row)">删除
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-collapse-item>
      <el-collapse-item>
        <template slot="title">
          <h4 class="left-title"> 已结束任务
          </h4>
        </template>
        <div class="finish-table">
          <el-table
            :data="finished"
            style="width: 100%">
            <el-table-column
              label="项目"
              prop="project"
              sortable
              min-width="10%"
              header-align="center"
            />
            <el-table-column
              label="爬虫"
              prop="spider"
              sortable
              min-width="10%"
              header-align="center"
            />
            <el-table-column
              label="id"
              prop="id"
              sortable
              min-width="25%"
              header-align="center"
            />
            <el-table-column
              label="开始时间"
              prop="start_time"
              sortable
              min-width="15%"
              header-align="center"
            />
            <el-table-column
              label="结束时间"
              prop="end_time"
              sortable
              min-width="15%"
              header-align="center"
            />
            <el-table-column
              label="执行时间"
              prop="exec_time"
              min-width="10%"
              header-align="center"
            />
            <el-table-column label="操作" header-align="center" min-width="15%">
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  type="danger"
                  @click="logShow(scope.row)">查看日志
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-collapse-item>
    </el-collapse>
    <el-dialog title="日志" :visible.sync="dialogTableVisible" width="80%" top="5vh">
      <div class="log-content">
         <pre v-highlight>
         <code class="left-text accesslog" v-html="logtext">
      </code>
    </pre>
      </div>
    </el-dialog>
  </div>
</template>

<script>
  import {
    listprojects,
    listjobs,
    listlog
  } from '../store/api'
  import {timeFormat, timeReduce} from '../utils/timeUtils'

  export default {
    name: 'Main',
    data() {
      return {
        pending: [],
        running: [],
        finished: [],
        dialogTableVisible: false,
        logtext: '',
        interval: 0,
        intervalid: 0,
        intervalid2: 0,
        intervaltext: '定时刷新'
      }
    },
    mounted() {
      this.loadTask()
    },
    methods: {
      // 加载所有任务
      loadTask() {
        this.$refs.topProgress.start()
        this.pending = []
        this.running = []
        this.finished = []
        listprojects().then(res => {
          let projectList = res.projects
          for (let project of projectList) {
            listjobs(project).then(res => {
              for (let pend of res.pending) {
                pend.project = project
                pend.start_time = timeFormat(pend.start_time)
                pend.end_time = timeFormat(pend.end_time)
                pend.exec_time = timeReduce(pend.start_time, null) + 's'
                this.pending.push(pend)
              }
              for (let run of res.running) {
                run.project = project
                run.start_time = timeFormat(run.start_time)
                run.end_time = timeFormat(run.end_time)
                run.exec_time = timeReduce(run.start_time, null) + 's'
                this.running.push(run)
              }
              for (let finish of res.finished) {
                finish.project = project
                finish.start_time = timeFormat(finish.start_time)
                finish.end_time = timeFormat(finish.end_time)
                finish.exec_time = timeReduce(finish.start_time, finish.end_time) + 's'
                this.finished.push(finish)
              }
              this.$refs.topProgress.done()
            })
          }
        }).catch(err => {
          console.log(err)
        })
      },
      // 显示日志
      logShow(job) {
        let param = {}
        param.ispaw = true
        param.project = job.project
        param.spider = job.spider
        param.id = job.id
        listlog(param).then(res => {
          this.logtext = (res.data.log_text).join('<br>')
          this.dialogTableVisible = true
        })
      },
      // 开始或停止自动刷新
      intervalLoadStartOrStop() {
        if (this.intervaltext === '定时刷新' && this.interval > 0) {
          this.intervalid = setInterval(() => {
            this.loadTask()
          }, this.interval * 1000)
          let timelimit = this.interval
          this.intervalid2 = setInterval(() => {
            timelimit = timelimit - 1
            if (timelimit === -1) {
              timelimit = this.interval
            }
            this.intervaltext = timelimit + '秒后刷新'
          }, 1000)
        } else {
          this.intervaltext = '定时刷新'
          this.interval = 0
          clearInterval(this.intervalid)
          clearInterval(this.intervalid2)
          this.intervalid = 0
          this.intervalid2 = 0
        }
      }
    },
    beforeDestroy() {
      clearInterval(this.intervalid)
      clearInterval(this.intervalid2)
    }
  }
</script>

<style scoped>
  .left-title {
    text-align: left !important;
    margin-left: 2%;
  }

  .left-text {
    text-align: left !important;
    margin-left: 2%;
  }

  .log-content {
    border: 1px sienna solid;
  }

  .main-content {
    border: 1px solid #ebebeb;
    border-radius: 3px;
    margin-top: 5px;
  }

  .button-tool {
    text-align: left;
    margin: 1% 0;
  }
</style>
