import { useState, useEffect } from "react";
// Antd
import { Typography } from "antd";
const { Paragraph } = Typography;

interface TypewriterProps {
  texts: string[];
  speed?: number;
  delay?: number; // New optional prop to set typing delay
}

const Typewriter: React.FC<TypewriterProps> = ({
  texts: textArray,
  speed = 100,
  delay = 0,
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
    if (typingCompleted) return;
    if (textArray.length === 0) {
      setTypingCompleted(true);
      return;
    }

    const startTyping = () => {
      const text = textArray[arrayIndex];

      const typingTimer = setTimeout(() => {
        setDisplayText((prev) => {
          const newPrev = [...prev];
          if (newPrev[arrayIndex]) {
            newPrev[arrayIndex] += text[charIndex];
          } else {
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
    };

    if (arrayIndex === 0 && charIndex === 0) {
      // Only apply delay for the first time a non-empty textArray is received
      const delayTimer = setTimeout(startTyping, delay);
      return () => clearTimeout(delayTimer);
    } else {
      startTyping();
    }
  }, [arrayIndex, charIndex, typingCompleted, textArray, delay]);

  return (
    <>
      {displayText.map((line, index) => (
        <Paragraph key={index}>{line}</Paragraph>
      ))}
    </>
  );
};

export default Typewriter;
