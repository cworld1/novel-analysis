import React from "react";
import { Avatar, Button, List, Tooltip, Typography } from "antd";
import { GithubOutlined, TwitterOutlined } from "@ant-design/icons";
const { Title, Paragraph } = Typography;

const AboutPage: React.FC = () => {
  const membersData = [
    {
      title: "CWorld",
      avatar:
        "https://cravatar.cn/avatar/1ffe42aa45a6b1444a786b1f32dfa8aa?s128",
      desc: "Data source request and front-end developing",
      links: {
        github: "https://github.com/cworld1",
        twitter: "https://twitter.com/cworld0",
      },
    },
    {
      title: "lilcookie11",
      desc: "Building a large language model and analyzing word recognition",
      links: {
        github: "https://github.com/lilcookie11",
      },
    },
    {
      title: "Boiyaaa",
      desc: "Api fetch",
      links: {
        github: "https://github.com/Boiyaaa",
      },
    },
    {
      title: "Mr. Xiao",
    },
  ];

  // Supported linktype and render actions
  type LinkType = { link?: string; logo: React.ReactNode; title: string };
  const renderAction = ({ link, logo, title }: LinkType) => {
    return link ? (
      <Tooltip placement="bottom" title={title}>
        <Button type="text">
          <a href={link} target="_blank" rel="noopener noreferrer">
            {logo}
          </a>
        </Button>
      </Tooltip>
    ) : null;
  };
  // Render member items
  const renderMemberListItem = (item: any, index: number) => {
    // Init link list to component list
    const links = [
      {
        link: item.links?.github,
        logo: <GithubOutlined />,
        title: "Github",
      },
      {
        link: item.links?.twitter,
        logo: <TwitterOutlined />,
        title: "Twitter",
      },
    ]
      .map((linkData) => renderAction(linkData))
      .filter(Boolean);

    return (
      <List.Item actions={links}>
        <List.Item.Meta
          avatar={
            <Avatar
              src={
                item.avatar ??
                `https://api.dicebear.com/7.x/miniavs/svg?seed=${index}`
              }
            />
          }
          title={item.title}
          description={item.desc ?? "Loaf on a job"}
        />
      </List.Item>
    );
  };

  return (
    <div>
      <Title>About</Title>

      <Title level={4}>Project</Title>
      <Paragraph>
        A simple project for analyzing Chinese novels. All data is crawled from{" "}
        <a href="https://www.hongxiu.com/">红袖读书</a>.
      </Paragraph>
      <Paragraph>For more infomations, please check our repository:</Paragraph>
      <Paragraph>
        <Button
          icon={<GithubOutlined />}
          onClick={() =>
            window.open("https://github.com/cworld1/novel_analysis", "_blank")
          }
        >
          Novel Analysis
        </Button>
      </Paragraph>

      <Title level={4}>Data</Title>
      <Paragraph>
        The repository following also contains the data, which has been a
        submodule part of this project.
      </Paragraph>
      <Paragraph>
        <Button
          icon={<GithubOutlined />}
          onClick={() =>
            window.open("https://github.com/cworld1/novel-data", "_blank")
          }
        >
          Novel Data
        </Button>
      </Paragraph>

      <Title level={4}>Team Members</Title>
      <List
        bordered
        itemLayout="horizontal"
        dataSource={membersData}
        renderItem={renderMemberListItem}
      ></List>
    </div>
  );
};

export default AboutPage;
