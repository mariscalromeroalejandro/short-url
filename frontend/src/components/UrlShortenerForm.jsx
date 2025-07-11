import React, { useState, useEffect, useRef } from 'react';
import UrlInput from './UrlInput';
import CustomAliasInput from './CustomAliasInput';
import ExpiryCheckbox from './ExpiryCheckbox';
import ExpiryDaysInput from './ExpiryDaysInput';
import ResultDisplay from './ResultDisplay';

export default function UrlShortenerForm() {
  const [longUrl, setLongUrl] = useState('');
  const [customAlias, setCustomAlias] = useState('');
  const [setExpiry, setSetExpiry] = useState(false);
  const [expiryDays, setExpiryDays] = useState(7);
  const [isValidUrl, setIsValidUrl] = useState(false);
  const [isValidExpiry, setIsValidExpiry] = useState(true);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [copyText, setCopyText] = useState('Copy');
  const copyTimeoutRef = useRef(null);


  // Validar días de expiración solo si está activado
  useEffect(() => {
    if (!setExpiry) {
      setIsValidExpiry(true);
      return;
    }
    const valid = expiryDays >= 1 && expiryDays <= 365;
    setIsValidExpiry(valid);
  }, [expiryDays, setExpiry]);

  const isFormValid = isValidUrl && isValidExpiry;

  async function handleSubmit(e) {
    e.preventDefault();

    if (!isFormValid) {
      alert('Please fill the form correctly.');
      return;
    }

    const payload = {
      long_url: longUrl,
      custom_alias: customAlias || null,
    };

    if (setExpiry) {
      const now = new Date();
      now.setDate(now.getDate() + expiryDays);
      payload.expiry_date = now.toISOString();
    }

    try {
      const res = await fetch('http://localhost:8000/api/urls', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      const data = await res.json();

      if (res.ok) {
        setResult(data.short_url);
        setError(null);
      } else {
        setError(data.detail || 'An error occurred.');
        setResult(null);
      }
    } catch {
      setError('Network error. Please try again later.');
      setResult(null);
    }
  }

  function handleCopy() {
    if (!result) return;
    navigator.clipboard.writeText(result).then(() => {
      setCopyText('Copied!');
      // avoid race conditions
      if (copyTimeoutRef.current) clearTimeout(copyTimeoutRef.current);
      copyTimeoutRef.current = setTimeout(() => {
        setCopyText('Copy');
        copyTimeoutRef.current = null;
      }, 2000);
    });
  }

  function handleShare(shortUrl) {
    if (!shortUrl) {
      alert('No hay URL para compartir');
      return;
    }
    const message = encodeURIComponent(`Check this out: ${shortUrl}`);
    const whatsappUrl = `https://wa.me/?text=${message}`;
    window.open(whatsappUrl, '_blank');
  }

  function validateUrl(value) {
    if (!value) return false;
    try {
      new URL(value);
      return true;
    } catch {
      return false;
    }
  }

  useEffect(() => {
    setIsValidUrl(validateUrl(longUrl));
  }, [longUrl]);

  useEffect(() => {
    return () => {
      if (copyTimeoutRef.current) {
        clearTimeout(copyTimeoutRef.current);
      }
    }
  }, [])

  return (
    <main className="container my-5">
      <section className="shortener-card mx-auto">
        <div className="shortener-card-body">
          <h3 className="fw-semibold mb-3">Shorten a Link</h3>
          <p className="text-muted mb-4">
            Paste a long URL and generate a shorter version to share easily.
          </p>

          <form onSubmit={handleSubmit}>
            <UrlInput
              value={longUrl}
              onChange={setLongUrl}
              setIsValidUrl={setIsValidUrl}
            />
            <CustomAliasInput value={customAlias} onChange={setCustomAlias} />
            <ExpiryCheckbox checked={setExpiry} onChange={setSetExpiry} />
            {setExpiry && (
              <ExpiryDaysInput value={expiryDays} onChange={setExpiryDays} />
            )}
            {!isValidExpiry && (
              <div className="text-danger mb-3">
                Please enter a valid number of days between 1 and 365.
              </div>
            )}
            {/* button to reset the form */}
            <button
              type="reset"
              className="btn shortener-btn-clear w-100"
              onClick={() => {
                setLongUrl('');
                setCustomAlias('');
                setSetExpiry(false);
                setExpiryDays(7);
                setIsValidUrl(false);
                setIsValidExpiry(true);
                setResult(null);
                setError(null);
              }}
            >
              Reset
            </button>
            <button
              type="submit"
              className="btn shortener-btn w-100"
              disabled={!isFormValid}
            >
              Shorten URL
            </button>
          </form>

          <ResultDisplay
            result={result}
            error={error}
            onCopy={handleCopy}
            copyText={copyText}
            onShare={() => handleShare(result)}
          />
        </div>
      </section>
    </main>
  );
}
