<template>
  <div class="task-list">
    <div class="pending-table">
      <h3 class="left-title">部署中任务</h3>
      <el-table
        :data="pending"
        style="width: 100%">
        <el-table-column
          label="项目"
          prop="project"
          sortable
          width="100"
          header-align="center"
        />
        <el-table-column
          label="爬虫"
          prop="spider"
          sortable
          width="100"
          header-align="center"
        />
        <el-table-column
          label="id"
          prop="id"
          sortable
          width="300"
          header-align="center"
        />
        <el-table-column
          label="开始时间"
          prop="start_time"
          sortable
          width="200"
          header-align="center"
        />
        <el-table-column
          label="结束时间"
          prop="end_time"
          sortable
          width="250"
          header-align="center"
        />
        <el-table-column
          label="执行时间"
          prop="exec_time"
          sortable
          width="100"
          header-align="center"
        />
        <el-table-column label="操作" header-align="center">
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
    <div class="running-table">
      <h3 class="left-title">进行中任务</h3>
      <el-table
        :data="running"
        style="width: 100%">
        <el-table-column
          label="项目"
          prop="project"
          sortable
          width="100"
          header-align="center"
        />
        <el-table-column
          label="爬虫"
          prop="spider"
          sortable
          width="100"
          header-align="center"
        />
        <el-table-column
          label="id"
          prop="id"
          sortable
          width="300"
          header-align="center"
        />
        <el-table-column
          label="开始时间"
          prop="start_time"
          sortable
          width="200"
          header-align="center"
        />
        <el-table-column
          label="结束时间"
          prop="end_time"
          sortable
          width="250"
          header-align="center"
        />
        <el-table-column
          label="执行时间"
          prop="exec_time"
          sortable
          width="100"
          header-align="center"
        />
        <el-table-column label="操作" header-align="center">
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
    <div class="finish-table">
      <h3 class="left-title">已结束任务</h3>
      <el-table
        :data="finished"
        style="width: 100%">
        <el-table-column
          label="项目"
          prop="project"
          sortable
          width="100"
          header-align="center"
        />
        <el-table-column
          label="爬虫"
          prop="spider"
          sortable
          width="100"
          header-align="center"
        />
        <el-table-column
          label="id"
          prop="id"
          sortable
          width="300"
          header-align="center"
        />
        <el-table-column
          label="开始时间"
          prop="start_time"
          sortable
          width="200"
          header-align="center"
        />
        <el-table-column
          label="结束时间"
          prop="end_time"
          sortable
          width="250"
          header-align="center"
        />
        <el-table-column
          label="执行时间"
          prop="exec_time"
          sortable
          width="100"
          header-align="center"
        />
        <el-table-column label="操作" header-align="center">
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
    <el-dialog title="日志" :visible.sync="dialogTableVisible">
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
  import {listprojects, listjobs, listlog} from '../store/api'
  import {timeFormat, timeReduce} from '../utils/timeUtils'

  export default {
    name: 'Main',
    data() {
      return {
        pending: [],
        running: [],
        finished: [],
        dialogTableVisible: false,
        logtext: ''
      }
    },
    mounted() {
      listprojects().then(res => {
        let projectList = res.projects
        for (let project of projectList) {
          listjobs(project).then(res => {
            for (let pend of res.pending) {
              pend.project = project
              this.pending.push(pend)
            }
            for (let run of res.running) {
              run.project = project
              this.running.push(run)
            }
            for (let finish of res.finished) {
              finish.project = project
              finish.start_time = timeFormat(finish.start_time)
              finish.end_time = timeFormat(finish.end_time)
              finish.exec_time = timeReduce(finish.start_time, finish.end_time) + 's'
              this.finished.push(finish)
            }
          })
        }
      }).catch(err => {
        console.log(err)
      })
    },
    methods: {
      logShow(job) {
        let param = {}
        param.ispaw = true
        param.path = 'e:/code/paw/logs'
        param.project = job.project
        param.spider = job.spider
        param.id = job.id
        listlog(param).then(res => {
          this.logtext = (res.data.log_text).join('<br>')
          this.dialogTableVisible = true
        })
      }
    }
  }
</script>

<style scoped>
  .left-title {
    text-align: left !important;
    margin-left: 10px;
  }

  .left-text {
    text-align: left !important;
    margin-left: 10px;
  }

  .log-content {
    border: 1px sienna solid;
  }
</style>
