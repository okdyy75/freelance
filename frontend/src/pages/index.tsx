import React from "react"
import { Heading, Text } from "theme-ui"

import Layout from "../layouts/layout"
import SEO from "../components/seo"
import Levtech from "../components/levtech"

const IndexPage = () => (
  <Layout>
    <SEO title="トップページ" />
    <Heading as="h2" variant="h2">
      About
    </Heading>
    <Text variant="p">
      このサイトはIT系フリーランスサイトから、プログラミング言語の単価を集計＆グラフ化したサイトです。
      <br />
      現在はレバテックフリーランスからのみ集計しています。
    </Text>
    <Levtech />
  </Layout>
)

export default IndexPage
