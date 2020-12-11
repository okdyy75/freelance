import React from "react"
import { Bar } from "react-chartjs-2"
import { Grid, Heading, Select, Checkbox, Label } from "theme-ui"
import "chartjs-plugin-datalabels"
const _ = require("lodash")

class CsvGraph extends React.Component {
  constructor(props) {
    super(props)
    const isPrice = props.isPrice === false ? false : true
    const isCount = props.isCount === false ? false : true
    const title = props.title
    const csvData = props.csvData
    const csvDates = props.csvDates || []
    const currentAt = props.currentAt
    const { graphData, graphOption } = this.getGraph(title, csvData, currentAt, isPrice, isCount)

    this.state = {
      title: title,
      currentAt: currentAt,
      isPrice: isPrice,
      isCount: isCount,
      graphData: graphData,
      graphOption: graphOption,
      csvData: csvData,
      csvDates: csvDates,
    }
  }

  /**
   * 対象日時変更
   */
  handleSelectChange = event => {
    const currentAt = event.target.value
    const { graphData, graphOption } = this.getGraph(
      this.state.title,
      this.state.csvData,
      currentAt,
      this.state.isPrice,
      this.state.isCount
    )
    this.setState({
      currentAt: currentAt,
      graphData: graphData,
      graphOption: graphOption,
    })
  }

  /**
   * 単価・案件数の表示チェックボックス変更
   */
  handleCheckboxChange = event => {
    const name = event.target.name
    const checked = event.target.checked

    /* eslint-disable-next-line */
    this.state[name] = checked

    const { graphData, graphOption } = this.getGraph(
      this.state.title,
      this.state.csvData,
      this.state.currentAt,
      this.state.isPrice,
      this.state.isCount
    )
    this.setState({
      [name]: checked,
      graphData: graphData,
      graphOption: graphOption,
    })
  }

  /**
   * グラフ描画
   *
   * @param   string  title
   * @param   Object  csvData
   * @param   date    filterAt
   * @param   Boolean  isPrice
   * @param   Boolean  isCount
   *
   * @return  Object  { graphData, graphOption }
   */
  getGraph = (title, csvData, filterAt, isPrice, isCount) => {
    let csvDataNodes = _.filter(csvData, (v, k) => v.created_at === filterAt)
    if (isPrice) {
      csvDataNodes = _.sortBy(csvDataNodes, (v, k) => -Number(v.avg_price))
    } else {
      csvDataNodes = _.sortBy(csvDataNodes, (v, k) => -Number(v.count))
    }
    const labels = csvDataNodes.map((v, k) => v.skill)
    const counts = csvDataNodes.map((v, k) => Number(v.count))
    const prices = csvDataNodes.map((v, k) => Number(v.avg_price))

    /** グラフデータ */
    let datasets = []
    if (isPrice) {
      datasets.push({
        type: "bar",
        yAxisID: "y-axis-1",
        data: prices,
        backgroundColor: "royalblue",
        label: "平均単価",
      })
    }
    if (isCount) {
      datasets.push({
        type: "bar",
        yAxisID: "y-axis-2",
        data: counts,
        backgroundColor: "orange",
        label: "案件数",
      })
    }
    const graphData = {
      labels: labels,
      datasets: datasets,
    }

    /** グラフオプション */
    const graphOption = {
      scales: {
        xAxes: [
          {
            scaleLabel: {
              display: false,
              labelString: title,
            },
          },
        ],
        yAxes: [
          {
            id: "y-axis-1",
            position: "left",
            offset: true,
            scaleLabel: {
              display: isPrice,
              labelString: "平均単価",
            },
          },
          {
            id: "y-axis-2",
            position: "right",
            scaleLabel: {
              display: isCount,
              labelString: "案件数",
            },
          },
        ],
      },
      plugins: {
        datalabels: {
          display: true,
          anchor: "end",
          align: "top",
          font: {
            size: 10,
          },
          padding: {
            top: -10,
          },
        },
      },
    }
    return { graphData, graphOption }
  }

  render() {
    return (
      <section>
        <Heading as="h3" variant="h3">
          {this.state.title}
        </Heading>
        {this.state.csvDates.length > 0 && (
          <Select mb={3} defaultValue={this.state.currentAt} onChange={this.handleSelectChange}>
            {this.state.csvDates.map((date, k) => (
              <option key={k} value={date}>
                {`${date.substr(0, 4)}年${date.substr(4, 2)}月`}
              </option>
            ))}
          </Select>
        )}
        <Grid columns={4}>
          <Label mb={3}>
            <Checkbox name="isPrice" defaultChecked={this.state.isPrice} onChange={this.handleCheckboxChange}></Checkbox>
            単価
          </Label>
          <Label mb={3}>
            <Checkbox name="isCount" defaultChecked={this.state.isCount} onChange={this.handleCheckboxChange}></Checkbox>
            案件数
          </Label>
        </Grid>
        <Bar data={this.state.graphData} options={this.state.graphOption} />
      </section>
    )
  }
}

export default CsvGraph
