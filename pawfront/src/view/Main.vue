<template>
  <div class="main-content">
    <div class="button-tool">
      <el-button type="primary" size="mini"
                 @click="dialogFormVisible = true" class="left-text">新增项目
      </el-button>
    </div>
    <el-collapse>
      <el-collapse-item>
        <template slot="title">
          <h4 class="left-title"> 项目列表
          </h4>
        </template>
        <div class="pending-table">
          <el-table
            :data="projects"
            style="width: 100%">
            <el-table-column
              label="名称"
              sortable
              prop="name"
              min-width="25%"
              header-align="center"
            />
            <el-table-column
              label="备注"
              prop="memo"
              min-width="25%"
              header-align="center"
            />
            <el-table-column
              label="路径"
              prop="path"
              min-width="25%"
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
    <el-dialog title="日志" :visible.sync="dialogTableVisible">
      <div class="log-content">
         <pre v-highlight>
         <code class="left-text accesslog" v-html="logtext">
      </code>
    </pre>
      </div>
    </el-dialog>
    <el-dialog title="新建项目" :visible.sync="dialogFormVisible">
      <el-form :model="project">
        <el-form-item label="项目名称" :label-width="formLabelWidth">
          <el-input v-model="project.name" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="项目备注" :label-width="formLabelWidth">
          <el-input v-model="project.memo" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="项目路径" :label-width="formLabelWidth">
          <el-input v-model="project.path" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="saveProject">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
  import {listprojects, listjobs, listlog, listdefinedprojects, saveproject} from '../store/api'
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
        projects: [],
        dialogFormVisible: false,
        project: {},
        formLabelWidth: '120px'
      }
    },
    mounted() {
      this.loadTask()
      this.listDefinedProjects()
    },
    methods: {
      listDefinedProjects() {
        let param = {}
        param.ispaw = true
        listdefinedprojects(param).then(res => {
          this.projects = res.data
        })
      },
      loadTask() {
        let param = {}
        param.ispaw = true
        listprojects(param).then(res => {
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
            })
          }
        }).catch(err => {
          console.log(err)
        })
      },
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
      },
      saveProject() {
        let param = {}
        param.ispaw = true
        param.path = this.project.path
        param.name = this.project.name
        param.memo = this.project.memo
        saveproject(param).then(res => {
          this.dialogFormVisible = false
          this.listDefinedProjects()
          this.$notify({
            title: '标题名称',
            message: res.msg
          })
        }).catch(err => {
          console.log(err)
        })
      }
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
