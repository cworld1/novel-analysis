import React, { useContext, useEffect, useState } from "react";
import axios from "axios";
// Antd
import { Collapse, CollapseProps, Flex, List, Typography } from "antd";
const { Title, Paragraph, Text } = Typography;
// Components
import { ConfigContext } from "../components/ConfigProvider";
import ChartComponent from "../components/Chart";

// Character interface
interface CharacterInfo {
  name: string;
  desc: string;
  characterDesc: string;
  develop: string;
  relationship: string;
  socialBackground: string;
  mbti: string;
  mbtiDesc: string;
  mbtiReasons: string[];
  mbtiRadar: any;
}

const BoardCharacterPage: React.FC = () => {
  const [characters, setCharacters] = useState<Array<CharacterInfo>>(
    Array<CharacterInfo>(5).fill({
      name: "",
      desc: "",
      characterDesc: "",
      develop: "",
      relationship: "",
      socialBackground: "",
      mbti: "",
      mbtiDesc: "",
      mbtiReasons: [],
      mbtiRadar: "{}",
    })
  );
  const { serverAddress } = useContext(ConfigContext);

  useEffect(() => {
    // Fetch character info
    axios
      .get<CharacterInfo[]>(`${serverAddress}/anal/character?name=longzu`)
      .then((response) => {
        setCharacters(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  const items: CollapseProps["items"] = characters?.map((character, index) => {
    return {
      key: String(index),
      label: character.name,
      children: [
        <Paragraph>{character.desc}</Paragraph>,
        <Paragraph>
          <Flex>
            <ChartComponent
              width={350}
              height={"auto"}
              option={JSON.parse(character.mbtiRadar)}
              forceWidth
            />
            <div style={{ marginLeft: 20, width: "100%" }}>
              <Title level={4}>
                Personality: {character.mbti}，{character.mbtiDesc}
              </Title>
              <List
                header={<Text>Evaluation</Text>}
                bordered
                dataSource={character.mbtiReasons}
                renderItem={(item) => <List.Item>{item}</List.Item>}
              />
            </div>
          </Flex>
        </Paragraph>,
        <Title level={4}>Character Description</Title>,
        <Paragraph>{character.characterDesc}</Paragraph>,
        <Title level={4}>Development in Novel</Title>,
        <Paragraph>{character.develop}</Paragraph>,
        <Title level={4}>Social Character Relationships</Title>,
        <Paragraph>{character.relationship}</Paragraph>,
        <Title level={4}>Social Character Background & Role in Novel</Title>,
        <Paragraph>{character.socialBackground}</Paragraph>,
      ],
    };
  });

  return (
    <>
      <Title>Character of Novel</Title>
      <Paragraph>
        Using the novel "Longzu" as an example for character analysis.
      </Paragraph>
      <Title level={3}>Specific analysis of novel characters</Title>
      <Collapse
        items={items}
        defaultActiveKey={["1"]}
        // onChange={onChange}
      />
    </>
  );
};

export default BoardCharacterPage;
