import { useState, useEffect } from "react";
// Antd
import { Typography } from "antd";
const { Paragraph } = Typography;

interface TypewriterProps {
  textArray: string[];
  typingSpeed?: number;
}

const Typewriter: React.FC<TypewriterProps> = ({
  textArray,
  typingSpeed = 100,
}) => {
  const [displayText, setDisplayText] = useState<string[]>([]);
  const [arrayIndex, setArrayIndex] = useState(0);
  const [charIndex, setCharIndex] = useState(0);
  const [typingCompleted, setTypingCompleted] = useState(false);

  useEffect(() => {
    if (!typingCompleted) {
      const text = textArray[arrayIndex];

      const timer = setTimeout(() => {
        setDisplayText((prev) => {
          const newPrev = [...prev];
          if (newPrev[arrayIndex]) {
            // If this line already exists, add a character at the end of this line
            newPrev[arrayIndex] += text[charIndex];
          } else {
            // If this line does not exist, create it and add characters
            newPrev[arrayIndex] = text[charIndex];
          }
          return newPrev;
        });

        if (charIndex < text.length - 1) {
          setCharIndex((prev) => prev + 1);
        } else if (arrayIndex < textArray.length - 1) {
          setArrayIndex((prev) => prev + 1);
          setCharIndex(0);
        } else {
          setTypingCompleted(true);
        }
      }, typingSpeed);

      return () => clearTimeout(timer);
    }
  }, [displayText, arrayIndex, charIndex, typingCompleted]);

  return (
    <Paragraph>
      {displayText.map((line, index) => (
        <>
          <span>{line}</span>
          <br />
        </>
      ))}
    </Paragraph>
  );
};

export default Typewriter;
