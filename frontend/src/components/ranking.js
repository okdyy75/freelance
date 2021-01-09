import React from "react"
import CsvGraph from "./csv-graph"
import { Heading, Grid, Box } from "theme-ui"

import "chartjs-plugin-datalabels"
const _ = require("lodash")

class Ranking extends React.Component {
  constructor(props) {
    super(props)
    const title = props.title
    const csvData = props.csvData
    const csvDates = props.csvDates

    this.state = {
      title: title,
      csvData: csvData,
      csvDates: csvDates,
    }
  }

  render() {
    return (
      <section>
        <Heading mt={5} as="h2" variant="h2">
          月別単価ランキング（2020年11月〜現在）
        </Heading>
        <Grid width={340}>
          {this.state.csvDates.map(date => {
            let title = `${date.substr(0, 4)}年${date.substr(4, 2)}月`
            let csvData = _.filter(this.state.csvData, (v, k) => v.created_at === date)
            csvData = _.sortBy(csvData, (v, k) => -Number(v.avg_price))
            // 10位まで表示
            csvData = csvData.slice(0, 10)
            return (
              <Box key={date}>
                <CsvGraph key={date} isCount={false} title={title} csvData={csvData} csvDates={[]} currentAt={date} />
              </Box>
            )
          })}
        </Grid>
      </section>
    )
  }
}

export default Ranking
