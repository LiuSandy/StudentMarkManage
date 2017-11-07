<template>
  <div>
    <Row>
      <Col span="7">
      <Card style="background:#23b7e5">
        <p slot="title">学生信息</p>
        <p style="color:#000000">学生人数：{{ studentInfo['allStudent'] }}</p>
        <p><br></p>
        <p style="color:#000000">及格率：{{ studentInfo['passRate'] }}</p>
        <p><br></p>
        <p style="color:#000000">课程总数：6</p>
        <p><br></p>
      </Card>
      </Col>
      <Col span="15" offset="1">
      <Table :columns="columns" :data="data" ref="table"></Table>
      <br>
      <Button type="primary" size="large" @click="exportData(1)">
        <Icon type="ios-download-outline"></Icon>
        导出原始数据
      </Button>
      <Button type="primary" size="large" @click="exportData(2)">
        <Icon type="ios-download-outline"></Icon>
        导出排序和过滤后的数据
      </Button>
      </Col>
    </Row>
    <Col span="7">
    <div id="myChart" :style="{height: '300px'}"></div>
    </Col>
    <Col span="15" offset="1">
    <Table :columns="columns1" :data="data1" style="margin-top: 5%" ref="table1"></Table>
    <br>
    <Button type="primary" size="large" @click="exportData(1)">
      <Icon type="ios-download-outline"></Icon>
      导出原始数据
    </Button>
    <Button type="primary" size="large" @click="exportData(2)">
      <Icon type="ios-download-outline"></Icon>
      导出排序和过滤后的数据
    </Button>
    </Col>
  </div>
</template>
<script>
  export default {
    data () {
      return {
        studentInfo: [],
        courseInfo: [],
        columns: [
          {
            title: '课程',
            key: 'course'
          },
          {
            title: '及格人数',
            key: 'pass',
            sortable: true
          },
          {
            title: '及格率',
            key: 'passRate',
            sortable: true
          }
        ],
        data: [],
        columns1: [
          {
            title: '课程',
            key: 'course'
          },
          {
            title: '及格',
            key: 'pass',
            sortable: true
          },
          {
            title: '良好',
            key: 'good',
            sortable: true
          },
          {
            title: '优秀',
            key: 'excellent',
            sortable: true
          }
        ],
        data1: []
      }
    },
    mounted () {
      this._getInfo()
      this._getCourseInfo()
    },
    methods: {
      _getInfo () {
        this.$http.get('/getInfo').then(response => {
          this.studentInfo = response.data
          for (let i in this.studentInfo.detail) {
            let item = {
              course: i,
              pass: this.studentInfo.detail[i][0],
              passRate: this.studentInfo.detail[i][1]
            }
            this.data.push(item)
          }
        })
      },
      _getCourseInfo () {
        this.$http.get('/getCourseInfo').then(response => {
          this.courseInfo = response.data
          for (let i in this.courseInfo) {
            let item = {
              course: i,
              pass: this.courseInfo[i][60][0],
              good: this.courseInfo[i][75][0],
              excellent: this.courseInfo[i][90][0]
            }
            this.data1.push(item)
          }
          let pieData = []
          for (let i in this.courseInfo) {
            let item = {
              value: this.courseInfo[i][90][0],
              name: i
            }
            pieData.push(item)
          }

          let myChart = this.$echarts.init(document.getElementById('myChart'))

          myChart.setOption({
            title: {
              text: '课程优秀率',
              subtext: '课程分数>90'
            },
            tooltip: {
              trigger: 'item',
              formatter: '{a} <br/>{b} : {c} ({d}%)'
            },
            series: [
              {
                name: '优秀率',
                type: 'pie',
                radius: '55%',
                center: ['50%', '60%'],
                data: pieData,
                itemStyle: {
                  emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                  }
                }
              }
            ]
          })
        })
      },
      exportData (type) {
        if (type === 1) {
          this.$refs.table.exportCsv({
            filename: '原始数据'
          })
        } else if (type === 2) {
          this.$refs.table.exportCsv({
            filename: '排序和过滤后的数据',
            original: false
          })
        }
      },
      exportData1 (type) {
        if (type === 1) {
          this.$refs.table1.exportCsv({
            filename: '原始数据'
          })
        } else if (type === 2) {
          this.$refs.table1.exportCsv({
            filename: '排序和过滤后的数据',
            original: false
          })
        }
      }
    }
  }
</script>
