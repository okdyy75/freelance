import React from "react"
import { useStaticQuery, graphql } from "gatsby"
import { Box, Heading } from "theme-ui"
import CsvGraph from "./csv-graph"
import Ranking from "./ranking"
const _ = require("lodash")

const Levtech = () => {
  const data = useStaticQuery(
    graphql`
      {
        csvDates: allLevtechLanguageCsv {
          distinct(field: created_at)
        }
        allLevtechLanguageCsv {
          nodes {
            skill
            count
            avg_price
            created_at
          }
        }
        allLevtechFrameworkCsv {
          nodes {
            skill
            count
            avg_price
            created_at
          }
        }
        allLevtechDbCsv {
          nodes {
            skill
            count
            avg_price
            created_at
          }
        }
        allLevtechCloudCsv {
          nodes {
            skill
            count
            avg_price
            created_at
          }
        }
      }
    `
  )

  let csvDates = []
  // 2020年11月と12月は日付固定
  csvDates.push(_.find(data.csvDates.distinct, (v, k) => v === "20201121"))
  csvDates.push(_.find(data.csvDates.distinct, (v, k) => v === "20201205"))
  _.each(data.csvDates.distinct, (v1, k1) => {
    if (!_.find(csvDates, (v2, k2) => v2.indexOf(v1.substr(0, 6)) !== -1)) {
      csvDates.push(v1)
    }
  })
  csvDates = _.sortBy(csvDates, (v, k) => -Number(v))

  const allCsv = [
    ...data.allLevtechLanguageCsv.nodes,
    ...data.allLevtechFrameworkCsv.nodes,
    ...data.allLevtechDbCsv.nodes,
    ...data.allLevtechCloudCsv.nodes,
  ]
  const currentAt = _.first(csvDates)

  return (
    <div>
      <Ranking csvData={allCsv} csvDates={csvDates} />
      <Heading mt={5} as="h2" variant="h2">
        スキル別
      </Heading>
      <Box mt={4} mb={3}>
        <CsvGraph title="言語" csvData={data.allLevtechLanguageCsv.nodes} csvDates={csvDates} currentAt={currentAt} />
      </Box>
      <Box mt={5} mb={3}>
        <CsvGraph title="フレームワーク" csvData={data.allLevtechFrameworkCsv.nodes} csvDates={csvDates} currentAt={currentAt} />
      </Box>
      <Box mt={5} mb={3}>
        <CsvGraph title="DB" csvData={data.allLevtechDbCsv.nodes} csvDates={csvDates} currentAt={currentAt} />
      </Box>
      <Box mt={5} mb={3}>
        <CsvGraph title="クラウド" csvData={data.allLevtechCloudCsv.nodes} csvDates={csvDates} currentAt={currentAt} />
      </Box>
    </div>
  )
}

export default Levtech
