import { useState, useEffect } from "react";
// Antd
import { Typography } from "antd";
const { Paragraph } = Typography;

interface TypewriterProps {
  textArray: string[];
  speed?: number;
  delay?: number; // New optional prop to set typing delay
}

const Typewriter: React.FC<TypewriterProps> = ({
  textArray,
  speed = 100,
  delay = 0, // By default, delay time is 0
}) => {
  const [displayText, setDisplayText] = useState<string[]>([]);
  const [arrayIndex, setArrayIndex] = useState(0);
  const [charIndex, setCharIndex] = useState(0);
  const [typingCompleted, setTypingCompleted] = useState(false);

  useEffect(() => {
    setDisplayText([]);
    setArrayIndex(0);
    setCharIndex(0);
    setTypingCompleted(false);
  }, [textArray]);

  useEffect(() => {
    if (typingCompleted || textArray.length == 0) return;
    // Always start with a delay timer, it will be 0 if no delay is specified
    const delayTimer = setTimeout(
      () => {
        const text = textArray[arrayIndex];

        const typingTimer = setTimeout(() => {
          setDisplayText((prev) => {
            const newPrev = [...prev];
            if (newPrev[arrayIndex]) {
              // If this line already exists, add a character at the end of this line
              newPrev[arrayIndex] += text[charIndex];
            } else {
              // If this line does not exist, create it and add character to it
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
        }, speed);

        return () => clearTimeout(typingTimer);
      },
      arrayIndex > 0 ? delay : 0
    );

    return () => clearTimeout(delayTimer);
  }, [arrayIndex, charIndex, typingCompleted, textArray]);

  return (
    <>
      {displayText.map((line, index) => (
        <Paragraph key={index}>{line}</Paragraph>
      ))}
    </>
  );
};

export default Typewriter;
