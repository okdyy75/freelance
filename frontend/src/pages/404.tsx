/** @jsx jsx */
import { jsx, Flex } from "theme-ui"

import Layout from "../layouts/layout"
import SEO from "../components/seo"
import Image from "../components/image"

const NotFoundPage = () => (
  <Layout>
    <SEO title="404: Not found" />
    <Flex>
      <div sx={{ mx: `auto` }} />
      <Image path={`not-found.png`} width={600} height={`auto`} />
      <div sx={{ mx: `auto` }} />
    </Flex>
  </Layout>
)

export default NotFoundPage
